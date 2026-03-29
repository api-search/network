---
aid: atlassian:atlassian-atlassiancreateabuildstatusforacommit
name: Create A Build Status For A Commit
tags:
- Commit statuses
humanURL: 
properties: []
description: >-
  Creates a new build status against the specified commit.<br><br>If the specified key already exists, the existing status object will<br>be overwritten.<br><br>Example:<br><br>```<br>curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-repo/commit/e10dae226959c2194f2b07b077c07762d93821cf/statuses/build/           -X POST -u jdoe -H 'Content-Type: application/json'           -d '{<br>    "key": "MY-BUILD",<br>    "state": "SUCCESSFUL",<br>    "description": "42 tests passed",<br>    ...

---
