---
aid: docusign:docusign-organizationexport-organizationexport-getbyexportid
name: Returns the results for single user list export request.
tags:
- UserExport
humanURL: 
properties: []
description: >-
  Returns the results for single user list export request.  - Required scopes: `user_read`  Given an export id, this method returns the results of a single user list export request. To get a list of all the export requests, use `getUserListExports`.  Note that the `metadata_url` property of the response from `createUserListExport` is a read-to-use HTTP GET request to get the status.  You can find the actual list of users at  `results[n].url` in the response.

---
