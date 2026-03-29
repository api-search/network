---
aid: atlassian:atlassian-atlassiansetcolumns
name: Set Columns
tags:
- Filters
humanURL: 
properties: []
description: >-
  Sets the columns for a filter. Only navigable fields can be set as columns. Use [Get fields](#api-rest-api-3-field-get) to get the list fields in Jira. A navigable field has `navigable` set to `true`.<br><br>The parameters for this resource are expressed as HTML form data. For example, in curl:<br><br>`curl -X PUT -d columns=summary -d columns=description https://your-domain.atlassian.net/rest/api/3/filter/10000/columns`<br><br>**[Permissions](#permissions) required:** Permission to access Ji...

---
