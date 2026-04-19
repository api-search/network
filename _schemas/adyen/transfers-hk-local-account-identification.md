---
description: HKLocalAccountIdentification schema from Adyen API
layout: schema
name: HKLocalAccountIdentification
properties_list:
- description: The 9- to 15-character bank account number (alphanumeric), without separators or whitespace. Starts with the 3-digit branch code.
  name: accountNumber
  type: string
- description: The 3-digit clearing code, without separators or whitespace.
  name: clearingCode
  type: string
- description: '**hkLocal**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-hk-local-account-identification-schema.json
slug: transfers-hk-local-account-identification
tags:
- Payments
- Financial Services
- Fintech
title: HKLocalAccountIdentification
---
