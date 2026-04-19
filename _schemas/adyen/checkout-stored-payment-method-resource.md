---
description: StoredPaymentMethodResource schema from Adyen API
layout: schema
name: StoredPaymentMethodResource
properties_list:
- description: The brand of the card.
  name: brand
  type: string
- description: The month the card expires.
  name: expiryMonth
  type: string
- description: The last two digits of the year the card expires. For example, **22** for the year 2022.
  name: expiryYear
  type: string
- description: The response code returned by an external system (for example after a provisioning operation).
  name: externalResponseCode
  type: string
- description: The token reference of a linked token in an external system (for example a network token reference).
  name: externalTokenReference
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
- description: The name of the issuer of token or card.
  name: issuerName
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
- description: 'Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. > Your reference must not include personally identifiable information (PII), for exam'
  name: shopperReference
  type: string
- description: 'Defines a recurring payment type. Allowed values: * `Subscription` – A transaction for a fixed or variable amount, which follows a fixed schedule. * `CardOnFile` – With a card-on-file (CoF) transactio'
  name: supportedRecurringProcessingModels
  type: array
- description: The type of payment method.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-stored-payment-method-resource-schema.json
slug: checkout-stored-payment-method-resource
tags:
- Payments
- Financial Services
- Fintech
title: StoredPaymentMethodResource
---
