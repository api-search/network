---
aid: atlassian:atlassian-atlassiancomparetwocommitdiffstats
name: Compare Two Commit Diff Stats
tags:
- Commits
humanURL: 
properties: []
description: >-
  Produces a response in JSON format with a record for every path<br>modified, including information on the type of the change and the<br>number of lines added and removed.<br><br>#### Single commit spec<br><br>If the `spec` argument to this API is a single commit, the diff is<br>produced against the first parent of the specified commit.<br><br>#### Two commit spec<br><br>Two commits separated by `..` may be provided as the `spec`, e.g.,<br>`3a8b42..9ff173`. When two commits are provided and th...

---
