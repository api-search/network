---
description: PaymentMethodGroup schema from Adyen API
layout: schema
name: PaymentMethodGroup
properties_list:
- description: The name of the group.
  name: name
  type: string
- description: Echo data to be used if the payment method is displayed as part of this group.
  name: paymentMethodData
  type: string
- description: The unique code of the group.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-method-group-schema.json
slug: checkout-payment-method-group
tags:
- Payments
- Financial Services
- Fintech
title: PaymentMethodGroup
---
