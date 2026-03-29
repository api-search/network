---
aid: atlassian:atlassian-atlassiancreateacommentonanissue
name: Create A Comment On An Issue
tags:
- Issue tracker
humanURL: 
properties: []
description: >-
  Creates a new issue comment.<br><br>```<br>$ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/issues/42/comments/ \<br>  -X POST -u evzijst \<br>  -H 'Content-Type: application/json' \<br>  -d '{"content": {"raw": "Lorem ipsum."}}'<br>```

---
