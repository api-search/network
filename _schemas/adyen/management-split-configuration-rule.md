---
description: SplitConfigurationRule schema from Adyen API
layout: schema
name: SplitConfigurationRule
properties_list:
- description: The currency condition that defines whether the split logic applies. Its value must be a three-character [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217).
  name: currency
  type: string
- description: 'The funding source condition of the payment method (only for cards). Possible values: **credit**, **debit**, or **ANY**.'
  name: fundingSource
  type: string
- description: 'The payment method condition that defines whether the split logic applies. Possible values: * [Payment method variant](https://docs.adyen.com/development-resources/paymentmethodvariant): Apply the spl'
  name: paymentMethod
  type: string
- description: The unique identifier of the split configuration rule.
  name: ruleId
  type: string
- description: 'The sales channel condition that defines whether the split logic applies. Possible values: * **Ecommerce**: Online transactions where the cardholder is present. * **ContAuth**: Card on file and/or sub'
  name: shopperInteraction
  type: string
- description: Contains the split logic that is applied if the rule conditions are met.
  name: splitLogic
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-split-configuration-rule-schema.json
slug: management-split-configuration-rule
tags:
- Payments
- Financial Services
- Fintech
title: SplitConfigurationRule
---
