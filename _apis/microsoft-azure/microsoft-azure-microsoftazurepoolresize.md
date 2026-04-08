---
aid: microsoft-azure:microsoft-azure-microsoftazurepoolresize
name: Microsoft Azure Changes The Number Of Compute Nodes That Are Assigned To A Pool
tags:
- Pools
humanURL: 
properties: []
description: >-
  You can only resize a Pool when its allocation state is steady. If the Pool is already resizing, the request fails with status code 409. When you resize a Pool, the Pool's allocation state changes from steady to resizing. You cannot resize Pools which are configured for automatic scaling. If you try to do this, the Batch service returns an error 409. If you resize a Pool downwards, the Batch service chooses which Compute Nodes to remove. To remove specific Compute Nodes, use the Pool remove C...

---
