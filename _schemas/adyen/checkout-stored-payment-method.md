---
description: StoredPaymentMethod schema from Adyen API
layout: schema
name: StoredPaymentMethod
properties_list:
- description: The bank account number (without separators).
  name: bankAccountNumber
  type: string
- description: The location id of the bank. The field value is `nil` in most cases.
  name: bankLocationId
  type: string
- description: The brand of the card.
  name: brand
  type: string
- description: The month the card expires.
  name: expiryMonth
  type: string
- description: The last two digits of the year the card expires. For example, **22** for the year 2022.
  name: expiryYear
  type: string
- description: The unique payment method code.
  name: holderName
  type: string
- description: The IBAN of the bank account.
  name: iban
  type: string
- description: A unique identifier of this stored payment method.
  name: id
  type: string
- description: The shopper’s issuer account label
  name: label
  type: string
- description: The last four digits of the PAN.
  name: lastFour
  type: string
- description: The display name of the stored payment method.
  name: name
  type: string
- description: Returned in the response if you are not tokenizing with Adyen and are using the Merchant-initiated transactions (MIT) framework from Mastercard or Visa. This contains either the Mastercard Trace ID or
  name: networkTxReference
  type: string
- description: The name of the bank account holder.
  name: ownerName
  type: string
- description: The shopper’s email address.
  name: shopperEmail
  type: string
- description: The supported recurring processing models for this stored payment method.
  name: supportedRecurringProcessingModels
  type: array
- description: The supported shopper interactions for this stored payment method.
  name: supportedShopperInteractions
  type: array
- description: The type of payment method.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-stored-payment-method-schema.json
slug: checkout-stored-payment-method
tags:
- Payments
- Financial Services
- Fintech
title: StoredPaymentMethod
---
