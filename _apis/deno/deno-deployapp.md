---
aid: deno:deno-deployapp
name: Create revision
tags:
- Revisions
humanURL: 
properties: []
description: >-
  Creates a new revision (deployment) for an application by uploading assets and optional configuration. Assets are key-value pairs where keys are file paths relative to /app/src and values describe file content as UTF-8 text, base64-encoded binary, or symlinks. The revision progresses through queued, building, and succeeded (or failed) states. Build progress can be tracked via the revisions progress endpoint.

---
