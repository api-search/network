---
description: ''
layout: schema
name: TradingPartner
properties_list:
- description: Trading partner identifier
  name: tradingPartnerId
  type: integer
- description: Trading partner name
  name: tradingPartnerName
  type: string
- description: Trading partner type
  name: tradingPartnerType
  type: string
- description: Trading partner site identifier
  name: tradingPartnerSiteId
  type: integer
- description: Site name
  name: tradingPartnerSiteName
  type: string
- description: EDI location code (DUNS, DUNS+4, etc.)
  name: ediLocationCode
  type: string
- description: EDI translator code
  name: ediTranslatorCode
  type: string
- description: Document standard
  name: documentStandard
  type: string
- description: List of enabled EDI transactions for this partner
  name: enabledTransactions
  type: array
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/ecommerce-gateway-trading-partner-schema.json
slug: ecommerce-gateway-trading-partner
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: TradingPartner
---
