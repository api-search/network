---
description: ''
layout: schema
name: Address
properties_list:
- description: Address line 1. If the any of the address line value is present but line 1 value is absent then blank value will be considered. <BR/> **Conditional Mandatory**<font color='red'>* </font> field - <BR/>
  name: line1
  type: string
- description: Address line 2. If the any of the address line value is present but line 2 value is absent then blank value will be considered. <BR/> This field is required if configured as **Business Mandatory**<fon
  name: line2
  type: string
- description: Address line 3. If the any of the address line value is present but line 3 value is absent then blank value will be considered. <BR/> This field is required if configured as **Business Mandatory**<fon
  name: line3
  type: string
- description: Address line 4. If the any of the address line value is present but line 4 value is absent then blank value will be considered. <BR/> This field is required if configured as **Business Mandatory**<fon
  name: line4
  type: string
- description: City (free text). <BR/> This field will be ignored and populated internally if given country is same as institution country, and city is configured to be auto populated in Card Management > Institutio
  name: city
  type: string
- description: State. <BR/> This field is required if configured as **Business Mandatory**<font color='red'>* </font> * If zip flag is configured at Institution level by selecting the 'Domestic Postal Code Mandatory
  name: state
  type: string
- description: Country Code. Expressed as a 2-letter (Alpha-2) country code as defined in ISO 3166. <BR/> **Conditional Mandatory**<font color='red'>* </font> field - <BR/> * Current Address country is required whil
  name: country
  type: string
- description: Zip Code. <BR/> **Conditional Mandatory**<font color='red'>* </font> field - <BR/> * Required if given country is same as 'institution country', and 'zip code' is configured as mandatory in 'Card Mana
  name: zipCode
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-address-schema.json
slug: mastercard-card-issuance-address
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Address
---
