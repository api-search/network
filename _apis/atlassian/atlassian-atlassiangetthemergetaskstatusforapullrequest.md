---
aid: atlassian:atlassian-atlassiangetthemergetaskstatusforapullrequest
name: Get The Merge Task Status For A Pull Request
tags:
- Pullrequests
humanURL: 
properties: []
description: >-
  When merging a pull request takes too long, the client receives a<br>task ID along with a 202 status code. The task ID can be used in a call<br>to this endpoint to check the status of a merge task.<br><br>```<br>curl -X GET https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-status/<br>```<br><br>If the merge task is not yet finished, a PENDING status will be returned.<br><br>```<br>HTTP/2 200<br>{<br>    "task_status": "PENDING",<br>    "links": {<br> ...

---
