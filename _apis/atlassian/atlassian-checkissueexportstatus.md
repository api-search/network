---
aid: atlassian:atlassian-checkissueexportstatus
name: Check Issue Export Status
tags:
- Checks
- Issues
- Exports
- Status
humanURL: 
properties: []
description: >-
  This GET operation checks the status of a previously initiated issue export request for a specific Bitbucket repository by polling the export endpoint using the provided task ID. When called, it queries the export job identified by the workspace, repository slug, repository name, and unique task identifier to determine whether the export process is still running, has completed successfully, or has failed. If the export is complete, the endpoint returns the ZIP file containing the exported iss...

---
