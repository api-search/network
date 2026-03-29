---
aid: cubefs:cubefs-deletevolume
name: Delete a volume
tags:
- Volumes
humanURL: 
properties: []
description: >-
  Marks a volume for deletion. The volume is first logically deleted by setting its status to deleted, then all data and metadata partitions are asynchronously removed via periodic tasks. Erasure-coded volumes can only be deleted when their used size is 0.

---
