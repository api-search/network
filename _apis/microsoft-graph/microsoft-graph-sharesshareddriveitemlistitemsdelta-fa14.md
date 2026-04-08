---
aid: microsoft-graph:microsoft-graph-sharesshareddriveitemlistitemsdelta-fa14
name: Microsoft Graph Invoke function delta
tags:
- Shares.list
humanURL: 
properties: []
description: >-
  Get newly created, updated, or deleted list items without having to perform a full read of the entire items collection. Your app begins by calling delta without any parameters. The service starts enumerating the hierarchy of the list, returning pages of items, and either an @odata.nextLink or an @odata.deltaLink. Your app should continue calling with the @odata.nextLink until you see an @odata.deltaLink returned. After you received all the changes, you can apply them to your local state. T...

---
