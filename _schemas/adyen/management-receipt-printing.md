---
description: ReceiptPrinting schema from Adyen API
layout: schema
name: ReceiptPrinting
properties_list:
- description: Print a merchant receipt when the payment is approved.
  name: merchantApproved
  type: boolean
- description: Print a merchant receipt when the transaction is cancelled.
  name: merchantCancelled
  type: boolean
- description: Print a merchant receipt when capturing the payment is approved.
  name: merchantCaptureApproved
  type: boolean
- description: Print a merchant receipt when capturing the payment is refused.
  name: merchantCaptureRefused
  type: boolean
- description: Print a merchant receipt when the refund is approved.
  name: merchantRefundApproved
  type: boolean
- description: Print a merchant receipt when the refund is refused.
  name: merchantRefundRefused
  type: boolean
- description: Print a merchant receipt when the payment is refused.
  name: merchantRefused
  type: boolean
- description: Print a merchant receipt when a previous transaction is voided.
  name: merchantVoid
  type: boolean
- description: Print a shopper receipt when the payment is approved.
  name: shopperApproved
  type: boolean
- description: Print a shopper receipt when the transaction is cancelled.
  name: shopperCancelled
  type: boolean
- description: Print a shopper receipt when capturing the payment is approved.
  name: shopperCaptureApproved
  type: boolean
- description: Print a shopper receipt when capturing the payment is refused.
  name: shopperCaptureRefused
  type: boolean
- description: Print a shopper receipt when the refund is approved.
  name: shopperRefundApproved
  type: boolean
- description: Print a shopper receipt when the refund is refused.
  name: shopperRefundRefused
  type: boolean
- description: Print a shopper receipt when the payment is refused.
  name: shopperRefused
  type: boolean
- description: Print a shopper receipt when a previous transaction is voided.
  name: shopperVoid
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-receipt-printing-schema.json
slug: management-receipt-printing
tags:
- Payments
- Financial Services
- Fintech
title: ReceiptPrinting
---
