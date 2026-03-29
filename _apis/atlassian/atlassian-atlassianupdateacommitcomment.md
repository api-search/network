---
aid: atlassian:atlassian-atlassianupdateacommitcomment
name: Update A Commit Comment
tags:
- Commits
humanURL: 
properties: []
description: >-
  Used to update the contents of a comment. Only the content of the comment can be updated.<br><br>```<br>$ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/commit/7f71b5/comments/5728901 \<br>  -X PUT -u evzijst \<br>  -H 'Content-Type: application/json' \<br>  -d '{"content": {"raw": "One more thing!"}'<br>```

---
