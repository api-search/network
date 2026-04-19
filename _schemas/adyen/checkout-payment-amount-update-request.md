---
description: PaymentAmountUpdateRequest schema from Adyen API
layout: schema
name: PaymentAmountUpdateRequest
properties_list:
- description: The updated amount. The `currency` must match the currency used in authorisation.
  name: amount
  type: object
- description: Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions).
  name: applicationInfo
  type: object
- description: 'The reason for the amount update. Possible values: * **delayedCharge** * **noShow** * **installment**'
  name: industryUsage
  type: string
- description: Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment). > This field is required for partial refunds with 3
  name: lineItems
  type: array
- description: The merchant account that is used to process the payment.
  name: merchantAccount
  type: string
- description: 'Your reference for the amount update request. Maximum length: 80 characters.'
  name: reference
  type: string
- description: An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For details, refer to [Providing split information](https://docs.adyen.com/marketplaces-a
  name: splits
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-amount-update-request-schema.json
slug: checkout-payment-amount-update-request
tags:
- Payments
- Financial Services
- Fintech
title: PaymentAmountUpdateRequest
---
