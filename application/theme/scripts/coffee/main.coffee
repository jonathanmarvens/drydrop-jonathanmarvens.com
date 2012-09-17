displayLatestGitHubCommits = ->
	github_commits = new $_GitHub_LC
		'callback': (data) ->
			$('span.home-github-commits-loading').html 'Please wait while the GitHub commits are loaded.'
			$.each data, (key, value) ->
				html_data =
					'<dt>' +
						'<a href="' + value.repo['html_url'] + '">' + value.repo['name'] + '</a>' +
					'</dt>' +
					'<dd>' +
						'<small>'
				$.each value.commits, (commit_key, commit_value) ->
					html_data +=
							'<code>&#64;' + commit_value['committer']['login'] + '</code> ' +
							'<i class="icon-arrow-right"></i> ' +
							'<code>' + commit_value['sha'].slice(0, 10) + '</code> ' +
							'<span class="boldify">with</span> ' +
							'<code>' + commit_value['commit']['message'] + '</code> ' +
							'<br>'
				html_data +=
					'</small>'
				html_data +=
					'</dd>' +
					'<hr>'

				if key is 0
					$('dl#home-latest-github-commits').html html_data
				else
					$('dl#home-latest-github-commits').append html_data

				return

			return
		'commit_count': 5
		'debug': 0
		'exclude_repos': ['twitter-bootstrap']
		'repo_count': 3
		'user': 'jonathanmarvens'
	.run()

	return

$(document).ready ->
	displayLatestGitHubCommits();

	return