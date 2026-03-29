---
aid: atlassian:atlassian-atlassiangetapatchfortwocommits
name: Get A Patch For Two Commits
tags:
- Commits
humanURL: 
properties: []
description: >-
  Produces a raw patch for a single commit (diffed against its first<br>parent), or a patch-series for a revspec of 2 commits (e.g.<br>`3a8b42..9ff173` where the first commit represents the source and the<br>second commit the destination).<br><br>In case of the latter (diffing a revspec), a patch series is returned<br>for the commits on the source branch (`3a8b42` and its ancestors in<br>our example).<br><br>While similar to diffs, patches:<br><br>* Have a commit header (username, commit messag...

---
