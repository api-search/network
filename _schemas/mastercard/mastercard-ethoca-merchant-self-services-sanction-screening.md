---
description: ''
layout: schema
name: SanctionScreening
properties_list:
- description: Known as VAT Number in the US and GST in Canada.
  name: taxId
  type: string
- description: The merchant's former legal names
  name: formerLegalNames
  type: array
- description: Indicates whether the merchant does business with sanctioned geographies. If it is true, then sanctionedGeographies property can't be empty.
  name: doBusinessWithSanctionedGeographies
  type: boolean
- description: List of sanctioned geographies that the merchant is doing business with. It can't be empty if the doBusinessWithSanctionedGeographies property is true
  name: sanctionedGeographies
  type: array
- description: Indicates whether a merchant is publicly traded.
  name: publiclyTraded
  type: boolean
- description: Publicly traded merchant's stock symbol. It's mandatory if the isPubliclyTraded attribute is true.
  name: tickerSymbol
  type: string
- description: Required only if publiclyTraded property is false and legalEntities property is empty.
  name: beneficialOwners
  type: array
- description: Required only if publiclyTraded property is false and beneficialOwners property is empty.
  name: legalEntities
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-ethoca-merchant-self-services-sanction-screening-schema.json
slug: mastercard-ethoca-merchant-self-services-sanction-screening
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: SanctionScreening
---
