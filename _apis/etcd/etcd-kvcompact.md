---
aid: etcd:etcd-kvcompact
name: Compact the event history
tags:
- KV
humanURL: 
properties: []
description: >-
  Compacts the etcd event history up to the given revision. All superseded keys with revisions less than the compaction revision are removed from the store, and watch operations cannot be made against compacted revisions. The physical option triggers a physical deletion of compacted keys immediately rather than deferring to the next compaction cycle.

---
