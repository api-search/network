---
description: CZLocalAccountIdentification schema from Adyen API
layout: schema
name: CZLocalAccountIdentification
properties_list:
- description: 'The 2- to 16-digit bank account number (Číslo účtu) in the following format: - The optional prefix (předčíslí). - The required second part (základní část) which must be at least two non-zero digits. E'
  name: accountNumber
  type: string
- description: The 4-digit bank code (Kód banky), without separators or whitespace.
  name: bankCode
  type: string
- description: '**czLocal**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-cz-local-account-identification-schema.json
slug: transfers-cz-local-account-identification
tags:
- Payments
- Financial Services
- Fintech
title: CZLocalAccountIdentification
---
