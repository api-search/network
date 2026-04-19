---
description: ListStoredPaymentMethodsResponse schema from Adyen API
layout: schema
name: ListStoredPaymentMethodsResponse
properties_list:
- description: Your merchant account.
  name: merchantAccount
  type: string
- description: 'Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. > Your reference must not include personally identifiable information (PII), for exam'
  name: shopperReference
  type: string
- description: List of all stored payment methods.
  name: storedPaymentMethods
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-list-stored-payment-methods-response-schema.json
slug: checkout-list-stored-payment-methods-response
tags:
- Payments
- Financial Services
- Fintech
title: ListStoredPaymentMethodsResponse
---
