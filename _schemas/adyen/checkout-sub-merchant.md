---
description: SubMerchant schema from Adyen API
layout: schema
name: SubMerchant
properties_list:
- description: 'The city of the sub-merchant''s address. * Format: Alphanumeric * Maximum length: 13 characters'
  name: city
  type: string
- description: 'The three-letter country code of the sub-merchant''s address. For example, **BRA** for Brazil. * Format: [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) * Fixed length: 3 charact'
  name: country
  type: string
- description: 'The sub-merchant''s 4-digit Merchant Category Code (MCC). * Format: Numeric * Fixed length: 4 digits'
  name: mcc
  type: string
- description: 'The name of the sub-merchant. Based on scheme specifications, this value will overwrite the shopper statement that will appear in the card statement. * Format: Alphanumeric * Maximum length: 22 charac'
  name: name
  type: string
- description: 'The tax ID of the sub-merchant. * Format: Numeric * Fixed length: 11 digits for the CPF or 14 digits for the CNPJ'
  name: taxId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-sub-merchant-schema.json
slug: checkout-sub-merchant
tags:
- Payments
- Financial Services
- Fintech
title: SubMerchant
---
