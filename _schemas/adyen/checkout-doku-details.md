---
description: DokuDetails schema from Adyen API
layout: schema
name: DokuDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The shopper's first name.
  name: firstName
  type: string
- description: The shopper's last name.
  name: lastName
  type: string
- description: The shopper's email.
  name: shopperEmail
  type: string
- description: '**doku**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-doku-details-schema.json
slug: checkout-doku-details
tags:
- Payments
- Financial Services
- Fintech
title: DokuDetails
---
