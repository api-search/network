---
aid: walmart:walmart-postshiporderlines
name: Walmart Ship one or more purchase order lines
tags:
- DSV Orders
humanURL: 
properties: []
description: >-
  <p style="color:red; font-size:larger">POST <walmartAuthServerUrl>/v3/orders/{purchaseOrderId}/shipping</p>  This request allows consumers to ship one or more purchase order (PO) lines.   For Site to Store (S2S) orders, package and pallet advance ship notices (ASN) need to be included in the request payload.  Changing the status of order lines to `Shipped` triggers a charge to the customer.  In order to avoid underselling, orders must be acknowledged before sending a shipping update.  Once an...

---
