---
aid: atlassian:atlassian-atlassianforkarepository
name: Fork A Repository
tags:
- Repositories
humanURL: 
properties: []
description: >-
  Creates a new fork of the specified repository.<br><br>#### Forking a repository<br><br>To create a fork, specify the workspace explicitly as part of the<br>request body:<br><br>```<br>$ curl -X POST -u jdoe https://api.bitbucket.org/2.0/repositories/atlassian/bbql/forks \<br>  -H 'Content-Type: application/json' -d '{<br>    "name": "bbql_fork",<br>    "workspace": {<br>      "slug": "atlassian"<br>    }<br>}'<br>```<br><br>To fork a repository into the same workspace, also specify a new `na...

---
