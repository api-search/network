---
aid: atlassian:atlassian-atlassianbulksetissuepropertiesbyissue
name: Bulk Set Issue Properties By Issue
tags:
- Issue properties
humanURL: 
properties: []
description: >-
  Sets or updates entity property values on issues. Up to 10 entity properties can be specified for each issue and up to 100 issues included in the request.<br><br>The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON.<br><br>This operation is:<br><br> *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.<br> *  non-t...

---
