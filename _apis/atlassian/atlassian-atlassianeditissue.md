---
aid: atlassian:atlassian-atlassianeditissue
name: Edit Issue
tags:
- Issues
humanURL: 
properties: []
description: >-
  Edits an issue. A transition may be applied and issue properties updated as part of the edit.<br><br>The edits to the issue's fields are defined using `update` and `fields`. The fields that can be edited are determined using [ Get edit issue metadata](#api-rest-api-3-issue-issueIdOrKey-editmeta-get).<br><br>The parent field may be set by key or ID. For standard issue types, the parent may be removed by setting `update.parent.set.none` to *true*. Note that the `description`, `environment`, and...

---
