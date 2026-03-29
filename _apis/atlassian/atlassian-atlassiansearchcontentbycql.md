---
aid: atlassian:atlassian-atlassiansearchcontentbycql
name: Search Content By Cql
tags:
- Content
humanURL: 
properties: []
description: >-
  Returns the list of content that matches a Confluence Query Language<br>(CQL) query. For information on CQL, see:<br>[Advanced searching using CQL](https://developer.atlassian.com/cloud/confluence/advanced-searching-using-cql/).<br><br>Example initial call:<br>```<br>/wiki/rest/api/content/search?cql=type=page&limit=25<br>```<br><br>Example response:<br>```<br>{<br>  "results": [<br>    { ... },<br>    { ... },<br>    ...<br>    { ... }<br>  ],<br>  "limit": 25,<br>  "size": 25,<br>  ...<br> ...

---
