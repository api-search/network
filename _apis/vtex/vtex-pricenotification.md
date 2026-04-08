---
aid: vtex:vtex-pricenotification
name: VTex Notify marketplace of price update
tags:
- Notification
humanURL: 
properties: []
description: >-
  This endpoint is used by *sellers* to notify marketplaces that the price has changed for one of their SKUs.   There is no request body in this call, indicating the new price value, for instance. It only notifies a specific marketplace (`accountName`) that a seller (`sellerId`) has changed the price of an SKU (`skuId`).   *Marketplaces* will then call the [fulfillment endpoint](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation) provided in the seller registration form ...

---
