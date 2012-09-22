displayLatestGitHubCommits = ->
	github_commits = new $_GitHub_LC
		'callback': (data) ->
			if data isnt false
				$('span.home-github-commits-loading').html 'Please wait while the GitHub commits are loaded.'
				$.each data, (key, value) ->
					html_data =
						'<dt>' +
							'<a href="' + value.repo['html_url'] + '">' + value.repo['name'] + '</a>' +
						'</dt>' +
						'<dd>' +
							'<small>'
					$.each value.commits, (commit_key, commit_value) ->
						# Same as moment(new Date(Date.parse(commit_value['commit']['committer']['date'])))
						commit_date = moment(Date.parse(commit_value['commit']['committer']['date']))
						commit_date = commit_date.fromNow()

						html_data +=
								'<br>' +
								'<a href="https://github.com/' + commit_value['committer']['login'] + '">' +
									'<code>&#64;' + commit_value['committer']['login'] + '</code>' +
								'</a> ' +
								'<i class="icon-arrow-right"></i> ' +
								'<a href="' + value.repo['html_url'] + '/commit/' + commit_value['sha'] + '">' +
									'<code>' + commit_value['sha'].slice(0, 10) + '</code>' +
								'</a> ' +
								'<span class="boldify">with</span> ' +
								'<code>' + commit_value['commit']['message'] + '</code> ' +
								'<br>' +
								'<small>' + commit_date + '</small>' +
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
		'exclude_repos': [
			'twitter-bootstrap'
		]
		'repo_count': 3
		'user': 'jonathanmarvens'
	.run()

	return

$(document).ready ->
	displayLatestGitHubCommits();

	$('a.lf_logo').remove();

	return