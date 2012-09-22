// Generated by CoffeeScript 1.3.3
var $_GitHub_LC;

$_GitHub_LC = (function() {

  function $_GitHub_LC(setup_options) {
    var available_option, available_options_keys, missing_option, _i, _j, _len, _len1, _ref;
    this.setup_options = setup_options;
    this.errors = false;
    this.available_options = {
      'callback': true,
      'commit_count': 3,
      'debug': 1,
      'exclude_repos': false,
      'repo_count': 5,
      'user': true
    };
    this.given_options = [];
    this.missing_options = [];
    this.user_github_repos_and_commits = [];
    this.user_github_commits_ajax_requests = [];
    if ($.isPlainObject(this.setup_options)) {
      available_options_keys = [];
      $.each(this.available_options, function(key, value) {
        return available_options_keys.push(key);
      });
      for (_i = 0, _len = available_options_keys.length; _i < _len; _i++) {
        available_option = available_options_keys[_i];
        if ($.inArray(available_option, this.setup_options)) {
          this.given_options.push(available_option);
        } else {
          this.missing_options.push(available_option);
          if (this.available_options[available_option] === true) {
            this.errors = true;
          }
        }
        _ref = this.missing_options;
        for (_j = 0, _len1 = _ref.length; _j < _len1; _j++) {
          missing_option = _ref[_j];
          this.setup_options[missing_option] = this.available_options[missing_option];
        }
      }
    } else {
      this.errors = true;
    }
  }

  $_GitHub_LC.prototype.get = function() {
    this.user_github_repos_and_commits.sort(function(a, b) {
      return Date.parse(b.repo['pushed_at']) - Date.parse(a.repo['pushed_at']);
    });
    return this.user_github_repos_and_commits;
  };

  $_GitHub_LC.prototype.run = function() {
    var github_api_users_user_repos_url, process_user_github_commits, user_github_repos,
      _this = this;
    if (this.errors === false) {
      user_github_repos = [];
      github_api_users_user_repos_url = 'https://api.github.com/users/' + this.setup_options['user'] + '/repos';
      $.ajax({
        'data': {
          'direction': 'desc',
          'sort': 'pushed',
          'type': 'all'
        },
        'dataType': 'jsonp',
        'error': function(jqXHR, status, error) {
          if (_this.setup_options['debug'] === 1) {
            console.log('Error receiving the GitHub repositories for the user "' + _this.setup_options['user'] + '"!');
            console.log('Status: ' + status + '.');
            console.log(error);
            console.log('jqXHR:');
            console.log(jqXHR);
          }
        },
        'success': function(data, status, jqXHR) {
          if (_this.setup_options['debug'] === 1) {
            console.log('Success receiving the GitHub repositories for the user "' + _this.setup_options['user'] + '"!');
            console.log('Status: ' + status);
            console.log(data);
            console.log('jqXHR:');
            console.log(jqXHR);
          }
          $('body').trigger('ajax_github_api_repos_success', data);
        },
        'url': github_api_users_user_repos_url
      });
      $('body').on('ajax_github_api_repos_success', function(event, data) {
        var exclude_repo, _i, _len, _ref;
        user_github_repos = data['data'];
        if ($.isArray(_this.setup_options['exclude_repos'])) {
          _ref = _this.setup_options['exclude_repos'];
          for (_i = 0, _len = _ref.length; _i < _len; _i++) {
            exclude_repo = _ref[_i];
            $.each(user_github_repos, function(key, value) {
              console.log(user_github_repos[key]);
              if (user_github_repos[key]['name'] === exclude_repo) {
                user_github_repos.splice(key, 1);
              }
            });
          }
        }
        user_github_repos.sort(function(a, b) {
          return Date.parse(b['pushed_at']) - Date.parse(a['pushed_at']);
        });
        process_user_github_commits();
      });
      process_user_github_commits = function() {
        var github_api_repos_user_repo_commits_url, user_github_repo, user_github_repos_and_commits_local, _i, _len;
        if (user_github_repos.length > _this.setup_options['repo_count']) {
          user_github_repos = user_github_repos.slice(0, _this.setup_options['repo_count']);
        }
        user_github_repos_and_commits_local = [];
        for (_i = 0, _len = user_github_repos.length; _i < _len; _i++) {
          user_github_repo = user_github_repos[_i];
          github_api_repos_user_repo_commits_url = 'https://api.github.com/repos/' + _this.setup_options['user'] + '/' + user_github_repo['name'] + '/commits';
          _this.user_github_commits_ajax_requests.push($.ajax({
            'ajax_data': {
              'user_github_repo': user_github_repo,
              'setup_options': _this.setup_options
            },
            'data': {
              'author': _this.setup_options['user']
            },
            'dataType': 'jsonp',
            'error': function(jqXHR, status, error) {
              if (this.ajax_data.setup_options['debug'] === 1) {
                console.log('Error receiving the commits for the GitHub repository ' + this.ajax_data.user_github_repo['name'] + ' which belongs to the user "' + this.ajax_data.setup_options['user'] + '"!');
                console.log('Status: ' + status + '.');
                console.log(error);
                console.log('jqXHR:');
                console.log(jqXHR);
              }
            },
            'success': function(data, status, jqXHR) {
              if (this.ajax_data.setup_options['debug'] === 1) {
                console.log('Success receiving the commits for the GitHub repository ' + this.ajax_data.user_github_repo['name'] + ' which belongs to the user "' + this.ajax_data.setup_options['user'] + '"!');
                console.log('Status: ' + status);
                console.log(data);
                console.log('jqXHR:');
                console.log(jqXHR);
              }
              data = data['data'];
              if (data.length > this.ajax_data.setup_options['commit_count']) {
                data = data.slice(0, this.ajax_data.setup_options['commit_count']);
              }
              user_github_repos_and_commits_local.push({
                'commits': data,
                'repo': this.ajax_data.user_github_repo
              });
            },
            'url': github_api_repos_user_repo_commits_url
          }));
        }
        $.when.apply($, _this.user_github_commits_ajax_requests).done(function() {
          _this.user_github_repos_and_commits = user_github_repos_and_commits_local;
          _this.setup_options['callback'](_this.get());
        });
      };
    } else {
      this.setup_options['callback'](false);
    }
  };

  return $_GitHub_LC;

})();
