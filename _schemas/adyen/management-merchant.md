---
description: Merchant schema from Adyen API
layout: schema
name: Merchant
properties_list:
- description: References to resources connected with this merchant.
  name: _links
  type: object
- description: 'The [capture delay](https://docs.adyen.com/online-payments/capture#capture-delay) set for the merchant account. Possible values: * **Immediate** * **Manual** * Number of days from **1** to **29**'
  name: captureDelay
  type: string
- description: The unique identifier of the company account this merchant belongs to
  name: companyId
  type: string
- description: List of available data centers. Adyen has several data centers around the world.In the URL that you use for making API requests, we recommend you use the live URL prefix from the data center closest t
  name: dataCenters
  type: array
- description: The default [`shopperInteraction`](https://docs.adyen.com/api-explorer/#/CheckoutService/v68/post/payments__reqParam_shopperInteraction) value used when processing payments through this merchant accou
  name: defaultShopperInteraction
  type: string
- description: Your description for the merchant account, maximum 300 characters
  name: description
  type: string
- description: The unique identifier of the merchant account.
  name: id
  type: string
- description: The city where the legal entity of this merchant account is registered.
  name: merchantCity
  type: string
- description: The name of the legal entity associated with the merchant account.
  name: name
  type: string
- description: Only applies to merchant accounts managed by Adyen's partners. The name of the pricing plan assigned to the merchant account.
  name: pricingPlan
  type: string
- description: 'The currency of the country where the legal entity of this merchant account is registered. Format: [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). For example, a lega'
  name: primarySettlementCurrency
  type: string
- description: Reference of the merchant account.
  name: reference
  type: string
- description: The URL for the ecommerce website used with this merchant account.
  name: shopWebAddress
  type: string
- description: 'The status of the merchant account. Possible values: * **PreActive**: The merchant account has been created. Users cannot access the merchant account in the Customer Area. The account cannot process p'
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-merchant-schema.json
slug: management-merchant
tags:
- Payments
- Financial Services
- Fintech
title: Merchant
---
