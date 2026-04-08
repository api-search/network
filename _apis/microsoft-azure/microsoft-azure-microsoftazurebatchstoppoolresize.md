---
aid: microsoft-azure:microsoft-azure-microsoftazurebatchstoppoolresize
name: Microsoft Azure Stops An Ongoing Resize Operation On The Pool
tags:
- Pools
humanURL: 
properties: []
description: >-
  This does not restore the Pool to its previous state before the resize<br>operation: it only stops any further changes being made, and the Pool maintains<br>its current state. After stopping, the Pool stabilizes at the number of Compute<br>Nodes it was at when the stop operation was done. During the stop operation,<br>the Pool allocation state changes first to stopping and then to steady. A<br>resize operation need not be an explicit resize Pool request; this API can also<br>be used to halt t...

---
