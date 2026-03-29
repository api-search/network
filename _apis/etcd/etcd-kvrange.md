---
aid: etcd:etcd-kvrange
name: Get a range of key-value pairs
tags:
- KV
humanURL: 
properties: []
description: >-
  Retrieves key-value pairs from the etcd cluster. A single key can be fetched by specifying only the key field. A range of keys can be fetched by specifying both key and range_end. Setting range_end to the key plus one byte fetches all keys with the given prefix. The limit parameter controls the maximum number of results returned, and the revision parameter enables point-in-time queries against a specific store revision.

---
