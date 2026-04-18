---
description: ''
layout: schema
name: refundPayment
properties_list:
- description: Unique refund payment Reference of the real time settlement method provided by CSP.
  name: refundpaymentReference
  type: string
- description: Creditor or CSP requested real-time settlement method. * Refer to Codes and Formats section for more details.
  name: clearingSystem
  type: string
- description: ''
  name: refundAmount
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-account-to-account-commerce-for-creditor-service-providers-refund-payment-schema.json
slug: mastercard-account-to-account-commerce-for-creditor-service-providers-refund-payment
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: refundPayment
---
