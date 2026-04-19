---
description: AdditionalBankIdentification schema from Adyen API
layout: schema
name: AdditionalBankIdentification
properties_list:
- description: The value of the additional bank identification.
  name: code
  type: string
- description: 'The type of additional bank identification, depending on the country. Possible values: * **gbSortCode**: The 6-digit [UK sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or spac'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-additional-bank-identification-schema.json
slug: transfers-additional-bank-identification
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalBankIdentification
---
