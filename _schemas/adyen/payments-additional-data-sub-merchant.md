---
description: AdditionalDataSubMerchant schema from Adyen API
layout: schema
name: AdditionalDataSubMerchant
properties_list:
- description: Required for transactions performed by registered payment facilitators. Indicates the number of sub-merchants contained in the request. For example, **3**.
  name: subMerchant.numberOfSubSellers
  type: string
- description: 'Required for transactions performed by registered payment facilitators. The city of the sub-merchant''s address. * Format: Alphanumeric * Maximum length: 13 characters'
  name: subMerchant.subSeller[subSellerNr].city
  type: string
- description: 'Required for transactions performed by registered payment facilitators. The three-letter country code of the sub-merchant''s address. For example, **BRA** for Brazil. * Format: [ISO 3166-1 alpha-3](htt'
  name: subMerchant.subSeller[subSellerNr].country
  type: string
- description: 'Required for transactions performed by registered payment facilitators. A unique identifier that you create for the sub-merchant, used by schemes to identify the sub-merchant. * Format: Alphanumeric *'
  name: subMerchant.subSeller[subSellerNr].id
  type: string
- description: 'Required for transactions performed by registered payment facilitators. The sub-merchant''s 4-digit Merchant Category Code (MCC). * Format: Numeric * Fixed length: 4 digits'
  name: subMerchant.subSeller[subSellerNr].mcc
  type: string
- description: Required for transactions performed by registered payment facilitators. The name of the sub-merchant. Based on scheme specifications, this value will overwrite the shopper statement that will appear i
  name: subMerchant.subSeller[subSellerNr].name
  type: string
- description: 'Required for transactions performed by registered payment facilitators. The postal code of the sub-merchant''s address, without dashes. * Format: Numeric * Fixed length: 8 digits'
  name: subMerchant.subSeller[subSellerNr].postalCode
  type: string
- description: 'Required for transactions performed by registered payment facilitators. The state code of the sub-merchant''s address, if applicable to the country. * Format: Alphanumeric * Maximum length: 2 character'
  name: subMerchant.subSeller[subSellerNr].state
  type: string
- description: 'Required for transactions performed by registered payment facilitators. The street name and house number of the sub-merchant''s address. * Format: Alphanumeric * Maximum length: 60 characters'
  name: subMerchant.subSeller[subSellerNr].street
  type: string
- description: 'Required for transactions performed by registered payment facilitators. The tax ID of the sub-merchant. * Format: Numeric * Fixed length: 11 digits for the CPF or 14 digits for the CNPJ'
  name: subMerchant.subSeller[subSellerNr].taxId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-additional-data-sub-merchant-schema.json
slug: payments-additional-data-sub-merchant
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalDataSubMerchant
---
