---
aid: atlassian:atlassian-atlassianlistcommitsthatmodifiedafile
name: List Commits That Modified A File
tags:
- Source - Repositories
humanURL: 
properties: []
description: >-
  Returns a paginated list of commits that modified the specified file.<br><br>Commits are returned in reverse chronological order. This is roughly<br>equivalent to the following commands:<br><br>    $ git log --follow --date-order  <br><br>By default, Bitbucket will follow renames and the path name in the<br>returned entries reflects that. This can be turned off using the<br>`?renames=false` query parameter.<br><br>Results are returned in descending chronological order by default, and<br>like ...

---
