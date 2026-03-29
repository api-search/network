---
aid: atlassian:atlassian-atlassianupdateanissue
name: Update An Issue
tags:
- Issue tracker
humanURL: 
properties: []
description: >-
  Modifies the issue.<br><br>```<br>$ curl https://api.bitbucket.org/2.0/repostories/evzijst/dogslow/issues/123 \<br>  -u evzijst -s -X PUT -H 'Content-Type: application/json' \<br>  -d '{<br>  "title": "Updated title",<br>  "assignee": {<br>    "account_id": "5d5355e8c6b9320d9ea5b28d"<br>  },<br>  "priority": "minor",<br>  "version": {<br>    "name": "1.0"<br>  },<br>  "component": null<br>}'<br>```<br><br>This example changes the `title`, `assignee`, `priority` and the<br>`version`. It also r...

---
