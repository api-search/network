---
aid: airbus-oneatlas:airbus-oneatlas-post-api-v1-deliveries
name: Deliver products
tags:
- Deliver
humanURL: 
properties: []
description: >-
  Deliver the requested catalog items to a workspace. The workspace may be configured to copy the items to an external data storage. This configuration can only be done via a non public endpoint. When delivered, each item emits a stage with name `ITEM_DELIVERED_TO_WORKSPACE`. When all items are delivered in the workspace, a stage with name `ALL_ITEMS_DELIVERED_TO_WORKSPACE` is emit.

---
