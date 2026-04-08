---
aid: qdrant:qdrant-schemaobjectsshardsupdate
name: Qdrant Update a shard status.
tags:
- Schema
humanURL: 
properties: []
description: >-
  Update a shard status for a collection. For example, a shard may have been marked as `READONLY` because its disk was full. After providing more disk space, use this endpoint to set the shard status to `READY` again. There is also a convenience function in each client to set the status of all shards of a collection.

---
