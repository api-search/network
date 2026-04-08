---
aid: vtex:vtex-inventorynotification
name: VTex Notify marketplace of inventory update
tags:
- Notification
humanURL: 
properties: []
description: >-
  This endpoint is used by *sellers* to notify marketplaces that the inventory level has changed for one of their SKUs.   There is no request body in this call, indicating the new inventory level, for instance. It only notifies a specific marketplace (`accountName`) that a seller (`sellerId`) has changed the inventory level of an SKU (`skuId`).   *Marketplaces* will then call the [fulfillment endpoint](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) provided in the s...

---
