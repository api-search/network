---
description: FundOrigin schema from Adyen API
layout: schema
name: FundOrigin
properties_list:
- description: The address where to send the invoice.
  name: billingAddress
  type: object
- description: Email address of the person.
  name: shopperEmail
  type: string
- description: The name of the person
  name: shopperName
  type: object
- description: Phone number of the person
  name: telephoneNumber
  type: string
- description: ''
  name: walletIdentifier
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-fund-origin-schema.json
slug: checkout-fund-origin
tags:
- Payments
- Financial Services
- Fintech
title: FundOrigin
---
