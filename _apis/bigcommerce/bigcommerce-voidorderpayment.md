---
aid: bigcommerce:bigcommerce-voidorderpayment
name: Void
tags:
- Payment Actions
humanURL: 
properties: []
description: >-
  Void the payment for an order. When there are no payment method validation issues, the void process is successful, the `payment_status` updates to `void pending`, and the void payment request is scheduled. The payment request itself occurs asynchronously.  Requires at least one of the following scopes: * `store_v2_orders` * `store_v2_transactions`

---
