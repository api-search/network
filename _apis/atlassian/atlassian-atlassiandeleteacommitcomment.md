---
aid: atlassian:atlassian-atlassiandeleteacommitcomment
name: Delete A Commit Comment
tags:
- Commits
humanURL: 
properties: []
description: >-
  Deletes the specified commit comment.<br><br>Note that deleting comments that have visible replies that point to<br>them will not really delete the resource. This is to retain the integrity<br>of the original comment tree. Instead, the `deleted` element is set to<br>`true` and the content is blanked out. The comment will continue to be<br>returned by the collections and self endpoints.

---
