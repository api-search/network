---
aid: walmart:walmart-postacknowledgeorders
name: Walmart Acknowledge orders
tags:
- DSV Orders
humanURL: 
properties: []
description: >-
  <p style="color:red; font-size:larger">POST <walmartAuthServerUrl>/v3/orders/{purchaseOrderId}/acknowledge</p>  This request allows a drop ship vendor (DSV) to acknowledge an order, including all order lines, preferably within four hours of receipt of the order.  The response to a successful call contains the acknowledged order.  As a good practice, acknowledge orders to avoid underselling.  Only those orders that are in a `Created` state should be acknowledged.  Orders that are in an `Acknow...

---
