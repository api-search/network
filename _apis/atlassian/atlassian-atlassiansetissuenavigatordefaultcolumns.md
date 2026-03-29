---
aid: atlassian:atlassian-atlassiansetissuenavigatordefaultcolumns
name: Set Issue Navigator Default Columns
tags:
- Issue navigator settings
humanURL: 
properties: []
description: >-
  Sets the default issue navigator columns.<br><br>The `columns` parameter accepts a navigable field value and is expressed as HTML form data. To specify multiple columns, pass multiple `columns` parameters. For example, in curl:<br><br>`curl -X PUT -d columns=summary -d columns=description https://your-domain.atlassian.net/rest/api/3/settings/columns`<br><br>If no column details are sent, then all default columns are removed.<br><br>A navigable field is one that can be used as a column on the ...

---
