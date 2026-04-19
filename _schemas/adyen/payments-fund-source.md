---
description: FundSource schema from Adyen API
layout: schema
name: FundSource
properties_list:
- description: A map of name-value pairs for passing additional or industry-specific data.
  name: additionalData
  type: object
- description: The address where to send the invoice.
  name: billingAddress
  type: object
- description: Credit card data. Optional if `shopperReference` and `selectedRecurringDetailReference` are provided.
  name: card
  type: object
- description: Email address of the person.
  name: shopperEmail
  type: string
- description: Name of the person.
  name: shopperName
  type: object
- description: Phone number of the person
  name: telephoneNumber
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-fund-source-schema.json
slug: payments-fund-source
tags:
- Payments
- Financial Services
- Fintech
title: FundSource
---
