---
aid: atlassian:atlassian-atlassiancomparetwocommits
name: Compare Two Commits
tags:
- Commits
humanURL: 
properties: []
description: >-
  Produces a raw git-style diff.<br><br>#### Single commit spec<br><br>If the `spec` argument to this API is a single commit, the diff is<br>produced against the first parent of the specified commit.<br><br>#### Two commit spec<br><br>Two commits separated by `..` may be provided as the `spec`, e.g.,<br>`3a8b42..9ff173`. When two commits are provided and the `topic` query<br>parameter is true, this API produces a 2-way three dot diff.<br>This is the diff between source commit and the merge base...

---
