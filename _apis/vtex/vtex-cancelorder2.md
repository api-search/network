---
aid: vtex:vtex-cancelorder2
name: VTex Cancel order
tags:
- Orders
humanURL: 
properties: []
description: >-
  You should use this endpoint to cancel an order by its `orderId`.  A common scenario is one where the seller has a problem with the order fulfillment and needs to request the order cancellation to the marketplace. To do this, the seller would need to make this request, passing the `orderId` in the URL.  You should expect a response with the date when the notification was received, the orderId, and a receipt protocol code.  Be aware that if the order status is already `Invoiced`, the order can...

---
