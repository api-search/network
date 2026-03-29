---
aid: atlassian:atlassian-atlassiansetusercolumns
name: Set User Default Columns
tags:
- Users
humanURL: 
properties: []
description: >-
  Sets the default [ issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user. If an account ID is not passed, the calling user's default columns are set. If no column details are sent, then all default columns are removed.<br><br>The parameters for this resource are expressed as HTML form data. For example, in curl:<br><br>`curl -X PUT -d columns=summary -d columns=description https://your-domain.atlassian.net/rest/api/3/user/columns?accountId=5b10ac8d82e05b22cc7d4ef5'`<br>...

---
