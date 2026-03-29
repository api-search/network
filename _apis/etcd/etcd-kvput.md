---
aid: etcd:etcd-kvput
name: Put a key-value pair
tags:
- KV
humanURL: 
properties: []
description: >-
  Stores a key-value pair in the etcd cluster. If the key already exists, the value is updated. Supports setting a lease ID to associate the key with a TTL-based lease that will delete the key when it expires. The prev_kv option returns the previous key-value pair before the update.

---
