---
aid: docker:docker-configupdate
name: Config Update
tags:
- Update
humanURL: 
properties: []
description: >-
  Updates an existing config by modifying its specification. This operation requires the config ID and version number to ensure safe concurrent updates. The request body contains the updated config specification including name, labels, and data, while the version parameter in the query string prevents conflicts from simultaneous modifications. Only certain fields like labels can be modified; the actual secret data itself cannot be changed after creation. The operation returns a 200 status code ...

---
