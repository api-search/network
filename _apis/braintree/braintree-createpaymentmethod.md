---
aid: braintree:braintree-createpaymentmethod
name: Create a payment method
tags:
- Payment Methods
humanURL: 
properties: []
description: >-
  Creates a new vaulted payment method for an existing customer using a payment method nonce obtained from the Braintree client SDK. The nonce is consumed and the underlying payment details are stored securely in the Braintree Vault. Returns a payment method object with a token that can be used for future transactions without requiring the customer to re-enter payment details.

---
