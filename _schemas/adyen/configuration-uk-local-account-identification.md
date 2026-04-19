---
description: UKLocalAccountIdentification schema from Adyen API
layout: schema
name: UKLocalAccountIdentification
properties_list:
- description: The 8-digit bank account number, without separators or whitespace.
  name: accountNumber
  type: string
- description: The 6-digit [sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or whitespace.
  name: sortCode
  type: string
- description: '**ukLocal**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-uk-local-account-identification-schema.json
slug: configuration-uk-local-account-identification
tags:
- Payments
- Financial Services
- Fintech
title: UKLocalAccountIdentification
---
