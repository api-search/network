---
description: CALocalAccountIdentification schema from Adyen API
layout: schema
name: CALocalAccountIdentification
properties_list:
- description: The 5- to 12-digit bank account number, without separators or whitespace.
  name: accountNumber
  type: string
- description: 'The bank account type. Possible values: **checking** or **savings**. Defaults to **checking**.'
  name: accountType
  type: string
- description: The 3-digit institution number, without separators or whitespace.
  name: institutionNumber
  type: string
- description: The 5-digit transit number, without separators or whitespace.
  name: transitNumber
  type: string
- description: '**caLocal**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-ca-local-account-identification-schema.json
slug: transfer-webhooks-ca-local-account-identification
tags:
- Payments
- Financial Services
- Fintech
title: CALocalAccountIdentification
---
