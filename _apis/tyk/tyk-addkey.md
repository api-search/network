---
aid: tyk:tyk-addkey
name: Tyk Create a key.
tags:
- Keys
humanURL: 
properties: []
description: >-
  Tyk will generate the access token based on the OrgID specified in the API Definition and a random UUID. This ensures that keys can be owned by different API Owners should segmentation be needed at an organisational level.  <br/><br/>   API keys without access_rights data will be written to all APIs on the system (this also means that they will be created across all SessionHandlers and StorageHandlers, it is recommended to always embed access_rights data in a key to ensure that only targeted ...

---
