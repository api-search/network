---
aid: atlassian:atlassian-atlassianupdateacommentonanissue
name: Update A Comment On An Issue
tags:
- Issue tracker
humanURL: 
properties: []
description: >-
  Updates the content of the specified issue comment. Note that only<br>the `content.raw` field can be modified.<br><br>```<br>$ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/issues/42/comments/5728901 \<br>  -X PUT -u evzijst \<br>  -H 'Content-Type: application/json' \<br>  -d '{"content": {"raw": "Lorem ipsum."}'<br>```

---
