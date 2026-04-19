---
description: NZLocalAccountIdentification schema from Adyen API
layout: schema
name: NZLocalAccountIdentification
properties_list:
- description: The 15-16 digit bank account number. The first 2 digits are the bank number, the next 4 digits are the branch number, the next 7 digits are the account number, and the final 2-3 digits are the suffix.
  name: accountNumber
  type: string
- description: '**nzLocal**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-nz-local-account-identification-schema.json
slug: transfers-nz-local-account-identification
tags:
- Payments
- Financial Services
- Fintech
title: NZLocalAccountIdentification
---
