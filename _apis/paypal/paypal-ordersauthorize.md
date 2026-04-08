---
aid: paypal:paypal-ordersauthorize
name: Paypal Authorize payment for order
tags:
- Orders
humanURL: 
properties: []
description: >-
  Authorizes payment for an order. To successfully authorize payment for an order, the buyer must first approve the order or a valid payment_source must be provided in the request. A buyer can approve the order upon being redirected to the rel:approve URL that was returned in the HATEOAS links in the create order response.<blockquote><strong>Note:</strong> For error handling and troubleshooting, see <a href="/api/rest/reference/orders/v2/errors/#authorize-order">Orders v2 errors</a>.</blockquote>

---
