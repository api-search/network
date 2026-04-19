---
description: BRLocalAccountIdentification schema from Adyen API
layout: schema
name: BRLocalAccountIdentification
properties_list:
- description: The bank account number, without separators or whitespace.
  name: accountNumber
  type: string
- description: The 3-digit bank code, with leading zeros.
  name: bankCode
  type: string
- description: The bank account branch number, without separators or whitespace.
  name: branchNumber
  type: string
- description: '**brLocal**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-br-local-account-identification-schema.json
slug: transfers-br-local-account-identification
tags:
- Payments
- Financial Services
- Fintech
title: BRLocalAccountIdentification
---
