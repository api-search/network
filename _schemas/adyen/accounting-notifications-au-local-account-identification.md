---
description: AULocalAccountIdentification schema from Adyen API
layout: schema
name: AULocalAccountIdentification
properties_list:
- description: The bank account number, without separators or whitespace.
  name: accountNumber
  type: string
- description: The 6-digit [Bank State Branch (BSB) code](https://en.wikipedia.org/wiki/Bank_state_branch), without separators or whitespace.
  name: bsbCode
  type: string
- description: '**auLocal**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounting-notifications-au-local-account-identification-schema.json
slug: accounting-notifications-au-local-account-identification
tags:
- Payments
- Financial Services
- Fintech
title: AULocalAccountIdentification
---
