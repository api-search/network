---
aid: tidb:tidb-gettableregions
name: Get table regions
tags:
- Regions
humanURL: 
properties: []
description: >-
  Returns the list of TiKV regions that store data for a specific TiDB table. Each region entry includes the region ID, start key, end key, leader peer, and follower peers. Use this endpoint to understand the physical data layout of a table across TiKV stores.

---
