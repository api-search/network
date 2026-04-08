---
aid: microsoft-azure:microsoft-azure-microsoftazureprivateendpointconnectionsgetgroupid
name: Microsoft Azure Returns Group Id Response 
this Is A Public Api Required By The Networking Rp Contract It Can Be Used Directly By Notification Hubs Users
tags:
- PrivateLink
humanURL: 
properties: []
description: >-
  Even though this namespace requires subscription id, resource group and namespace name, it returns a constant payload (for a given namespacE) every time it's called.<br>That's why we don't send it to the sibling RP, but process it directly in the scale unit that received the request.

---
