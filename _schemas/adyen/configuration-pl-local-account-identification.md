---
description: PLLocalAccountIdentification schema from Adyen API
layout: schema
name: PLLocalAccountIdentification
properties_list:
- description: The 26-digit bank account number ([Numer rachunku](https://pl.wikipedia.org/wiki/Numer_Rachunku_Bankowego)), without separators or whitespace.
  name: accountNumber
  type: string
- description: '**plLocal**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-pl-local-account-identification-schema.json
slug: configuration-pl-local-account-identification
tags:
- Payments
- Financial Services
- Fintech
title: PLLocalAccountIdentification
---
