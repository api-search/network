---
aid: microsoft-azure:microsoft-azure-microsoftazurebatchresizepool
name: Microsoft Azure Changes The Number Of Compute Nodes That Are Assigned To A Pool
tags:
- Pools
humanURL: 
properties: []
description: >-
  You can only resize a Pool when its allocation state is steady. If the Pool is<br>already resizing, the request fails with status code 409. When you resize a<br>Pool, the Pool's allocation state changes from steady to resizing. You cannot<br>resize Pools which are configured for automatic scaling. If you try to do this,<br>the Batch service returns an error 409. If you resize a Pool downwards, the<br>Batch service chooses which Compute Nodes to remove. To remove specific Compute<br>Nodes, use...

---
