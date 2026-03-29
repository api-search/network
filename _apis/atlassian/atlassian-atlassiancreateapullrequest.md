---
aid: atlassian:atlassian-atlassiancreateapullrequest
name: Create A Pull Request
tags:
- Pullrequests
humanURL: 
properties: []
description: >-
  Creates a new pull request where the destination repository is<br>this repository and the author is the authenticated user.<br><br>The minimum required fields to create a pull request are `title` and<br>`source`, specified by a branch name.<br><br>```<br>curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-repository/pullrequests \<br>    -u my-username:my-password \<br>    --request POST \<br>    --header 'Content-Type: application/json' \<br>    --data '{<br>        "title": "My ...

---
