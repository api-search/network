---
aid: bigcommerce:bigcommerce-createcheckouttoken
name: Create Checkout Token
tags:
- Checkout Token
humanURL: 
properties: []
description: >-
  Use the checkout token to display a confirmation page for a guest shopper. **Usage Notes** * The response from performing this POST request is a checkout token. * The checkout token is a single-use token that is not order-dependent. You cannot create this token after finalizing an order. * After completing the order, you can redirect the shopper to /order-confirmation/{orderId}?t={checkoutToken}. * After token validation, the /order-confirmation/{orderId} page displays. * The `ORDER_TOKEN` sh...

---
