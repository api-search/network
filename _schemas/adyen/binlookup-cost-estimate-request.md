---
description: CostEstimateRequest schema from Adyen API
layout: schema
name: CostEstimateRequest
properties_list:
- description: The transaction amount used as a base for the cost estimation.
  name: amount
  type: object
- description: Assumptions made for the expected characteristics of the transaction, for which the charges are being estimated.
  name: assumptions
  type: object
- description: The card number (4-19 characters) for PCI compliant use cases. Do not use any separators. > Either the `cardNumber` or `encryptedCardNumber` field must be provided in a payment request.
  name: cardNumber
  type: string
- description: Encrypted data that stores card information for non PCI-compliant use cases. The encrypted data must be created with the Checkout Card Component or Secured Fields Component, and must contain the `encr
  name: encryptedCardNumber
  type: string
- description: The merchant account identifier you want to process the (transaction) request with.
  name: merchantAccount
  type: string
- description: Additional data for merchants who don't use Adyen as the payment authorisation gateway.
  name: merchantDetails
  type: object
- description: The recurring settings for the payment. Use this property when you want to enable [recurring payments](https://docs.adyen.com/online-payments/tokenization).
  name: recurring
  type: object
- description: The `recurringDetailReference` you want to use for this cost estimate. The value `LATEST` can be used to select the most recently stored recurring detail.
  name: selectedRecurringDetailReference
  type: string
- description: Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer. For the web service API, Adyen assumes Ecommerce shopper interaction b
  name: shopperInteraction
  type: string
- description: 'Required for recurring payments. Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. > Your reference must not include personally identif'
  name: shopperReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/binlookup-cost-estimate-request-schema.json
slug: binlookup-cost-estimate-request
tags:
- Payments
- Financial Services
- Fintech
title: CostEstimateRequest
---
