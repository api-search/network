---
description: UpdateSplitConfigurationRuleRequest schema from Adyen API
layout: schema
name: UpdateSplitConfigurationRuleRequest
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
- description: 'The sales channel condition that defines whether the split logic applies. Possible values: * **Ecommerce**: Online transactions where the cardholder is present. * **ContAuth**: Card on file and/or sub'
  name: shopperInteraction
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-update-split-configuration-rule-request-schema.json
slug: management-update-split-configuration-rule-request
tags:
- Payments
- Financial Services
- Fintech
title: UpdateSplitConfigurationRuleRequest
---
