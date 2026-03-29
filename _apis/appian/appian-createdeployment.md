---
aid: appian:appian-createdeployment
name: Export or import a deployment
tags:
- Export
- Import
humanURL: 
properties: []
description: >-
  Creates a new deployment operation for either exporting or importing applications and packages. The Action-Type header determines whether the operation is an export or import. For exports, provide a JSON payload specifying the UUIDs and export type. For imports, provide a multipart form with the package files and deployment configuration. The response includes a deployment UUID that can be used to track progress and retrieve results.

---
