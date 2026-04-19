---
description: Avs schema from Adyen API
layout: schema
name: Avs
properties_list:
- description: Indicates whether the shopper is allowed to modify the billing address for the current payment request.
  name: addressEditable
  type: boolean
- description: 'Specifies whether the shopper should enter their billing address during checkout. Allowed values: * yes — Perform AVS checks for every card payment. * automatic — Perform AVS checks only when required'
  name: enabled
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-avs-schema.json
slug: checkout-avs
tags:
- Payments
- Financial Services
- Fintech
title: Avs
---
