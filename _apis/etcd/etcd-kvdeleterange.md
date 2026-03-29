---
aid: etcd:etcd-kvdeleterange
name: Delete a range of key-value pairs
tags:
- KV
humanURL: 
properties: []
description: >-
  Deletes one or more key-value pairs from the etcd cluster. A single key can be deleted by specifying only the key field. A range of keys is deleted by specifying both key and range_end. The prev_kv option returns the deleted key-value pairs before deletion. The count-only option returns only the count of deleted keys without performing the actual deletion.

---
