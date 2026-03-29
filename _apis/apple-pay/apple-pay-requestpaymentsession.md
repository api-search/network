---
aid: apple-pay:apple-pay-requestpaymentsession
name: Request an Apple Pay payment session
tags:
- Merchant Validation
humanURL: 
properties: []
description: >-
  Validates the merchant and returns an opaque payment session object. The merchant server calls this endpoint when the client-side ApplePaySession triggers the onvalidatemerchant event. The response must be passed back to the client via session.completeMerchantValidation(). Requires mutual TLS authentication using the merchant identity certificate.

---
