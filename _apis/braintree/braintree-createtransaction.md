---
aid: braintree:braintree-createtransaction
name: Create a transaction
tags:
- Transactions
humanURL: 
properties: []
description: >-
  Creates a new payment transaction (sale) through the Braintree gateway. Requires either a payment_method_nonce for a one-time payment method, a payment_method_token referencing a vaulted payment method, or a customer_id to use the customer's default vaulted payment method. The amount must be a positive decimal value matching the currency format. Optionally submit the transaction immediately for settlement or hold it in an authorized state for later capture.

---
