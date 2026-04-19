---
description: CheckoutSessionInstallmentOption schema from Adyen API
layout: schema
name: CheckoutSessionInstallmentOption
properties_list:
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
schema_file: json-schema/checkout-checkout-session-installment-option-schema.json
slug: checkout-checkout-session-installment-option
tags:
- Payments
- Financial Services
- Fintech
title: CheckoutSessionInstallmentOption
---
