---
aid: bigcommerce:bigcommerce-getpaymentmethods
name: Get Accepted Payment Methods
tags:
- Payments
- Methods
humanURL: 
properties: []
description: >-
  Returns a list of accepted payment methods based on the `order_id` or `checkout_id`.  **Notes** * Use the [Create an Order](/docs/rest-management/orders#create-an-order) endpoint to generate the `order_id`. * Orders created will be set to incomplete order status. * The cart ID and checkout ID are the same.  **Required Fields** * `order_id` or `checkout_id`

---
