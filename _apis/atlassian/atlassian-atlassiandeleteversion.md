---
aid: atlassian:atlassian-atlassiandeleteversion
name: Delete Version
tags:
- Project versions
humanURL: 
properties: []
description: >-
  Deletes a project version.<br><br>Deprecated, use [ Delete and replace version](#api-rest-api-3-version-id-removeAndSwap-post) that supports swapping version values in custom fields, in addition to the swapping for `fixVersion` and `affectedVersion` provided in this resource.<br><br>Alternative versions can be provided to update issues that use the deleted version in `fixVersion` or `affectedVersion`. If alternatives are not provided, occurrences of `fixVersion` and `affectedVersion` that con...

---
