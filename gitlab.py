# pip install python-gitlab

import gitlab
import pprint

git = gitlab.Gitlab(private_token="glpat-jojo-jojo")
l = git.projects.list(get_all=True, membership=True)
pprint.pprint(sorted([x.web_url for x in l]))

# pip install PyGithub

import github
git = github.Github(auth=github.Auth.Token("github_pat_jojojo"))
l = g.get_user('jojo').get_repos('all')
pprint.pprint(sorted([x.git_url for x in l]))
