---
description: SGLocalAccountIdentification schema from Adyen API
layout: schema
name: SGLocalAccountIdentification
properties_list:
- description: The 4- to 19-digit bank account number, without separators or whitespace.
  name: accountNumber
  type: string
- description: The bank's 8- or 11-character BIC or SWIFT code.
  name: bic
  type: string
- description: '**sgLocal**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-sg-local-account-identification-schema.json
slug: transfers-sg-local-account-identification
tags:
- Payments
- Financial Services
- Fintech
title: SGLocalAccountIdentification
---
