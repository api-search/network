---
aid: atlassian:atlassian-atlassianlistcommitsforrevision
name: List Commits For Revision
tags:
- Commits
humanURL: 
properties: []
description: >-
  These are the repository's commits. They are paginated and returned<br>in reverse chronological order, similar to the output of `git log`.<br>Like these tools, the DAG can be filtered.<br><br>#### GET /repositories/{workspace}/{repo_slug}/commits/master<br><br>Returns all commits on ref `master` (similar to `git log master`).<br><br>#### GET /repositories/{workspace}/{repo_slug}/commits/dev?include=foo&exclude=master<br><br>Returns all commits on ref `dev` or `foo`, except those that are reac...

---
