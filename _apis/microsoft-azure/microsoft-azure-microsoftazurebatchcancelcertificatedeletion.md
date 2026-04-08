---
aid: microsoft-azure:microsoft-azure-microsoftazurebatchcancelcertificatedeletion
name: Microsoft Azure Cancels A Failed Deletion Of A Certificate From The Specified Account
tags:
- certificates(thumbprintAlgorithm={thumbprintAlgorithm},thumbprint={thumbprint})
humanURL: 
properties: []
description: >-
  If you try to delete a Certificate that is being used by a Pool or Compute<br>Node, the status of the Certificate changes to deleteFailed. If you decide that<br>you want to continue using the Certificate, you can use this operation to set<br>the status of the Certificate back to active. If you intend to delete the<br>Certificate, you do not need to run this operation after the deletion failed.<br>You must make sure that the Certificate is not being used by any resources, and<br>then you can t...

---
