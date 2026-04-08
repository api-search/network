---
aid: microsoft-azure:microsoft-azure-microsoftazurepooldelete
name: Microsoft Azure Deletes A Pool From The Specified Account
tags:
- Pools
humanURL: 
properties: []
description: >-
  When you request that a Pool be deleted, the following actions occur: the Pool state is set to deleting; any ongoing resize operation on the Pool are stopped; the Batch service starts resizing the Pool to zero Compute Nodes; any Tasks running on existing Compute Nodes are terminated and requeued (as if a resize Pool operation had been requested with the default requeue option); finally, the Pool is removed from the system. Because running Tasks are requeued, the user can rerun these Tasks by ...

---
