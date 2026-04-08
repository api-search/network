---
aid: rook:rook-deleteobject
name: Rook Delete an object
tags:
- Objects
humanURL: 
properties: []
description: >-
  Deletes the specified object from the S3 bucket. If versioning is enabled, this creates a delete marker rather than permanently removing the object. The operation is idempotent and returns HTTP 204 even if the object does not exist.

---
