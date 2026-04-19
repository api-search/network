---
description: StoredValueBalanceMergeRequest schema from Adyen API
layout: schema
name: StoredValueBalanceMergeRequest
properties_list:
- description: The amount information for the transaction.
  name: amount
  type: object
- description: The merchant account identifier, with which you want to process the transaction.
  name: merchantAccount
  type: string
- description: The collection that contains the type of the payment method and its specific information if available
  name: paymentMethod
  type: object
- description: ''
  name: recurringDetailReference
  type: string
- description: The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a require
  name: reference
  type: string
- description: Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer. For the web service API, Adyen assumes Ecommerce shopper interaction b
  name: shopperInteraction
  type: string
- description: ''
  name: shopperReference
  type: string
- description: The collection that contains the source payment method and its specific information if available. Note that type should not be included since it is inferred from the (target) payment method
  name: sourcePaymentMethod
  type: object
- description: The physical store, for which this payment is processed.
  name: store
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/stored-value-stored-value-balance-merge-request-schema.json
slug: stored-value-stored-value-balance-merge-request
tags:
- Payments
- Financial Services
- Fintech
title: StoredValueBalanceMergeRequest
---
