---
description: SELocalAccountIdentification schema from Adyen API
layout: schema
name: SELocalAccountIdentification
properties_list:
- description: The 7- to 10-digit bank account number ([Bankkontonummer](https://sv.wikipedia.org/wiki/Bankkonto)), without the clearing number, separators, or whitespace.
  name: accountNumber
  type: string
- description: The 4- to 5-digit clearing number ([Clearingnummer](https://sv.wikipedia.org/wiki/Clearingnummer)), without separators or whitespace.
  name: clearingNumber
  type: string
- description: '**seLocal**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-se-local-account-identification-schema.json
slug: legal-entity-se-local-account-identification
tags:
- Payments
- Financial Services
- Fintech
title: SELocalAccountIdentification
---
