class $_GitHub_LC
	constructor: (@setup_options) ->
		@errors				= false
		@available_options	=
			'callback': true
			'commit_count': 3
			'debug': 1
			'exclude_repos': false
			'repo_count': 5
			'user': true
		@given_options		= []
		@missing_options	= []

		@user_github_repos_and_commits = []
		@user_github_commits_ajax_requests = []

		if $.isPlainObject @setup_options
			available_options_keys = []

			$.each @available_options, (key, value) ->
				available_options_keys.push key

			for available_option in available_options_keys
				if $.inArray available_option, @setup_options
					@given_options.push available_option
				else
					@missing_options.push available_option
					if @available_options[available_option] is true
						@errors = true

				for missing_option in @missing_options
					@setup_options[missing_option] = @available_options[missing_option]
		else
			@errors = true
	get: ->
		@user_github_repos_and_commits.sort (a, b) ->
			return Date.parse(b.repo['pushed_at']) - Date.parse a.repo['pushed_at']

		return @user_github_repos_and_commits
	run: ->
		if @errors is false
			user_github_repos = []

			github_api_users_user_repos_url = 'https://api.github.com/users/' + @setup_options['user'] + '/repos'

			$.ajax
				'data':
					'direction': 'desc'
					'sort': 'pushed'
					'type': 'all'
				'dataType': 'jsonp'
				'error': (jqXHR, status, error) =>
					if @setup_options['debug'] is 1
						console.log 'Error receiving the GitHub repositories for the user "' + @setup_options['user'] + '"!'
						console.log 'Status: ' + status + '.'
						console.log error
						console.log 'jqXHR:'
						console.log jqXHR

					return
				'success': (data, status, jqXHR) =>
					if @setup_options['debug'] is 1
						console.log 'Success receiving the GitHub repositories for the user "' + @setup_options['user'] + '"!'
						console.log 'Status: ' + status
						console.log data
						console.log 'jqXHR:'
						console.log jqXHR

					$('body').trigger 'ajax_github_api_repos_success', data

					return
				'url': github_api_users_user_repos_url

			$('body').on 'ajax_github_api_repos_success', (event, data) =>
				user_github_repos = data['data']

				if $.isArray @setup_options['exclude_repos']
					for exclude_repo in @setup_options['exclude_repos']
						$.each user_github_repos, (key, value) ->
							console.log value

							if value isnt undefined
								if value['name'] is exclude_repo
									user_github_repos.splice key, 1

							return

				user_github_repos.sort (a, b) ->
					return Date.parse(b['pushed_at']) - Date.parse a['pushed_at']

				process_user_github_commits()

				return

			process_user_github_commits = =>
				if user_github_repos.length > @setup_options['repo_count']
					user_github_repos = user_github_repos.slice 0, @setup_options['repo_count']

				user_github_repos_and_commits_local = []

				for user_github_repo in user_github_repos
					github_api_repos_user_repo_commits_url = 'https://api.github.com/repos/' + @setup_options['user'] + '/' + user_github_repo['name'] + '/commits'

					@user_github_commits_ajax_requests.push $.ajax
						'ajax_data':
							'user_github_repo': user_github_repo
							'setup_options': @setup_options
						'data':
							'author': @setup_options['user']
						'dataType': 'jsonp'
						'error': (jqXHR, status, error) ->
							if this.ajax_data.setup_options['debug'] is 1
								console.log 'Error receiving the commits for the GitHub repository ' + this.ajax_data.user_github_repo['name'] + ' which belongs to the user "' + this.ajax_data.setup_options['user'] + '"!'
								console.log 'Status: ' + status + '.'
								console.log error
								console.log 'jqXHR:'
								console.log jqXHR

							return
						'success': (data, status, jqXHR) ->
							if this.ajax_data.setup_options['debug'] is 1
								console.log 'Success receiving the commits for the GitHub repository ' + this.ajax_data.user_github_repo['name'] + ' which belongs to the user "' + this.ajax_data.setup_options['user'] + '"!'
								console.log 'Status: ' + status
								console.log data
								console.log 'jqXHR:'
								console.log jqXHR

							data = data['data']

							if data.length > this.ajax_data.setup_options['commit_count']
								data = data.slice 0, this.ajax_data.setup_options['commit_count']

							user_github_repos_and_commits_local.push
								'commits': data
								'repo': this.ajax_data.user_github_repo

							return
						'url': github_api_repos_user_repo_commits_url

				$.when.apply($, @user_github_commits_ajax_requests).done =>
					@user_github_repos_and_commits = user_github_repos_and_commits_local

					@setup_options['callback'] @get()

					return

				return
		else
			@setup_options['callback'] false
		return