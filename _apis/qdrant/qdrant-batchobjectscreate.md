---
aid: qdrant:qdrant-batchobjectscreate
name: Qdrant Batch create new objects.
tags:
- Batch
humanURL: 
properties: []
description: >-
  Create new objects in bulk. <br/><br/>Meta-data and schema values are validated. <br/><br/>**Note: idempotence of `/batch/objects`**: <br/>`POST /batch/objects` is idempotent, and will overwrite any existing object given the same id.

---
