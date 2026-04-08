---
aid: microsoft-azure:microsoft-azure-microsoftazurecertificatedelete
name: Microsoft Azure Deletes A Certificate From The Specified Account
tags:
- Certificates
humanURL: 
properties: []
description: >-
  You cannot delete a Certificate if a resource (Pool or Compute Node) is using it. Before you can delete a Certificate, you must therefore make sure that the Certificate is not associated with any existing Pools, the Certificate is not installed on any Nodes (even if you remove a Certificate from a Pool, it is not removed from existing Compute Nodes in that Pool until they restart), and no running Tasks depend on the Certificate. If you try to delete a Certificate that is in use, the deletion ...

---
