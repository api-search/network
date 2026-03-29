---
aid: amazon-web-services:amazon-web-services-amazonwebservicesbatchdeleterecipeversion
name: Batchdeleterecipeversion
tags:
- API
humanURL: 
properties: []
description: >-
  Deletes one or more versions of a recipe at a time. The entire request will be rejected if:   The recipe does not exist.   There is an invalid version identifier in the list of versions.   The version list is empty.   The version list size exceeds 50.   The version list contains duplicate entries.   The request will complete successfully, but with partial failures, if:   A version does not exist.   A version is being used by a job.   You specify LATEST_WORKING, but it's being used by a projec...

---
