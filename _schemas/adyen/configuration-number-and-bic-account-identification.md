---
description: NumberAndBicAccountIdentification schema from Adyen API
layout: schema
name: NumberAndBicAccountIdentification
properties_list:
- description: The bank account number, without separators or whitespace. The length and format depends on the bank or country.
  name: accountNumber
  type: string
- description: Additional identification codes of the bank. Some banks may require these identifiers for cross-border transfers.
  name: additionalBankIdentification
  type: object
- description: The bank's 8- or 11-character BIC or SWIFT code.
  name: bic
  type: string
- description: '**numberAndBic**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-number-and-bic-account-identification-schema.json
slug: configuration-number-and-bic-account-identification
tags:
- Payments
- Financial Services
- Fintech
title: NumberAndBicAccountIdentification
---
