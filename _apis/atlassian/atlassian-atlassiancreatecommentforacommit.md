---
aid: atlassian:atlassian-atlassiancreatecommentforacommit
name: Create Comment For A Commit
tags:
- Commits
humanURL: 
properties: []
description: >-
  Creates new comment on the specified commit.<br><br>To post a reply to an existing comment, include the `parent.id` field:<br><br>```<br>$ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/commit/db9ba1e031d07a02603eae0e559a7adc010257fc/comments/ \<br>  -X POST -u evzijst \<br>  -H 'Content-Type: application/json' \<br>  -d '{"content": {"raw": "One more thing!"},<br>       "parent": {"id": 5728901}}'<br>```

---
