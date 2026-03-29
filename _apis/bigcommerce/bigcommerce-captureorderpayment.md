---
aid: bigcommerce:bigcommerce-captureorderpayment
name: Capture order payment
tags:
- Payment Actions
humanURL: 
properties: []
description: >-
  Capture the payment for an order. When there are no payment method validation issues, the capture process is successful, the `payment_status` updates to `capture pending`, and the payment request is scheduled. The payment request itself occurs asynchronously. Requires at least one of the following scopes: * `store_v2_orders` * `store_v2_transactions`

---
