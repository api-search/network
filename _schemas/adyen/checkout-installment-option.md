---
description: InstallmentOption schema from Adyen API
layout: schema
name: InstallmentOption
properties_list:
- description: The maximum number of installments offered for this payment method.
  name: maxValue
  type: integer
- description: 'Defines the type of installment plan. If not set, defaults to **regular**. Possible values: * **regular** * **revolving**'
  name: plans
  type: array
- description: Preselected number of installments offered for this payment method.
  name: preselectedValue
  type: integer
- description: An array of the number of installments that the shopper can choose from. For example, **[2,3,5]**. This cannot be specified simultaneously with `maxValue`.
  name: values
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-installment-option-schema.json
slug: checkout-installment-option
tags:
- Payments
- Financial Services
- Fintech
title: InstallmentOption
---
