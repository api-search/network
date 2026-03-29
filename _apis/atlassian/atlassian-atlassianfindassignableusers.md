---
aid: atlassian:atlassian-atlassianfindassignableusers
name: Find Users Assignable To Issues
tags:
- User search
humanURL: 
properties: []
description: >-
  Returns a list of users that can be assigned to an issue. Use this operation to find the list of users who can be assigned to:<br><br> *  a new issue, by providing the `projectKeyOrId`.<br> *  an updated issue, by providing the `issueKey`.<br> *  to an issue during a transition (workflow action), by providing the `issueKey` and the transition id in `actionDescriptorId`. You can obtain the IDs of an issue's valid transitions using the `transitions` option in the `expand` parameter of [ Get iss...

---
