---
aid: atlassian:atlassian-atlassiancreatearepository
name: Create A Repository
tags:
- Repositories
humanURL: 
properties: []
description: >-
  Creates a new repository.<br><br>Note: In order to set the project for the newly created repository,<br>pass in either the project key or the project UUID as part of the<br>request body as shown in the examples below:<br><br>```<br>$ curl -X POST -H "Content-Type: application/json" -d '{<br>    "scm": "git",<br>    "project": {<br>        "key": "MARS"<br>    }<br>}' https://api.bitbucket.org/2.0/repositories/teamsinspace/hablanding<br>```<br><br>or<br><br>```<br>$ curl -X POST -H "Content-Ty...

---
