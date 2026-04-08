---
aid: walmart:walmart-postcancelorderlines
name: Walmart Cancel order lines
tags:
- DSV Orders
humanURL: 
properties: []
description: >-
  <p style="color:red; font-size:larger">POST <walmartAuthServerUrl>/v3/orders/{purchaseOrderId}/cancel</p>  This request cancels one or more order lines before an order has been fulfilled.   A `purchaseOrderId` must be included to cancel an order line.  Update the inventory after canceling an order.  The response to a successful call contains the order with the canceled line item.  Supported cancellation reasons include: * SUPPLIER_CANCEL_CUSTOMER_REQUEST * SUPPLIER_CANCEL_BACKORDER * SUPPLIER...

---
