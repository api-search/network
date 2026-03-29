---
aid: atlassian:atlassian-atlassianmergeversions
name: Merge Versions
tags:
- Project versions
humanURL: 
properties: []
description: >-
  Merges two project versions. The merge is completed by deleting the version specified in `id` and replacing any occurrences of its ID in `fixVersion` with the version ID specified in `moveIssuesTo`.<br><br>Consider using [ Delete and replace version](#api-rest-api-3-version-id-removeAndSwap-post) instead. This resource supports swapping version values in `fixVersion`, `affectedVersion`, and custom fields.<br><br>This operation can be accessed anonymously.<br><br>**[Permissions](#permissions) ...

---
