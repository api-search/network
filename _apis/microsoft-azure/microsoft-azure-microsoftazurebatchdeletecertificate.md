---
aid: microsoft-azure:microsoft-azure-microsoftazurebatchdeletecertificate
name: Microsoft Azure Deletes A Certificate From The Specified Account
tags:
- certificates(thumbprintAlgorithm={thumbprintAlgorithm},thumbprint={thumbprint})
humanURL: 
properties: []
description: >-
  You cannot delete a Certificate if a resource (Pool or Compute Node) is using<br>it. Before you can delete a Certificate, you must therefore make sure that the<br>Certificate is not associated with any existing Pools, the Certificate is not<br>installed on any Nodes (even if you remove a Certificate from a Pool, it is not<br>removed from existing Compute Nodes in that Pool until they restart), and no<br>running Tasks depend on the Certificate. If you try to delete a Certificate<br>that is in ...

---
