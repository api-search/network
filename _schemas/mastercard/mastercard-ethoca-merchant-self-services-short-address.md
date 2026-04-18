---
description: Address.
layout: schema
name: ShortAddress
properties_list:
- description: The street detail for the address.
  name: addressLine1
  type: string
- description: The secondary street detail for the address.
  name: addressLine2
  type: string
- description: Region where merchant's legal office is located
  name: regionCode
  type: string
- description: City where merchant's legal office is located
  name: city
  type: string
- description: The zip/postal detail for the merchant's legal address
  name: postalCode
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-ethoca-merchant-self-services-short-address-schema.json
slug: mastercard-ethoca-merchant-self-services-short-address
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: ShortAddress
---
