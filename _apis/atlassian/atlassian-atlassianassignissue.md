---
aid: atlassian:atlassian-atlassianassignissue
name: Assign Issue
tags:
- Issues
humanURL: 
properties: []
description: >-
  Assigns an issue to a user. Use this operation when the calling user does not have the *Edit Issues* permission but has the *Assign issue* permission for the project that the issue is in.<br><br>If `name` or `accountId` is set to:<br><br> *  `"-1"`, the issue is assigned to the default assignee for the project.<br> *  `null`, the issue is set to unassigned.<br><br>This operation can be accessed anonymously.<br><br>**[Permissions](#permissions) required:**<br><br> *  *Browse Projects* and *Ass...

---
