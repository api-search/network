---
description: ''
layout: schema
name: OutboundTransaction
properties_list:
- description: Transaction identifier
  name: transactionId
  type: integer
- description: Outbound transaction type code
  name: transactionType
  type: string
- description: Transaction description
  name: transactionDescription
  type: string
- description: Document standard (X12 or EDIFACT)
  name: documentStandard
  type: string
- description: ASC X12/EDIFACT document number
  name: documentNumber
  type: string
- description: ''
  name: tradingPartnerId
  type: integer
- description: ''
  name: tradingPartnerName
  type: string
- description: ''
  name: tradingPartnerSiteId
  type: integer
- description: ''
  name: processStatus
  type: string
- description: Source document identifier in Oracle EBS
  name: sourceDocumentId
  type: integer
- description: Source document number
  name: sourceDocumentNumber
  type: string
- description: ''
  name: documentDate
  type: string
- description: ''
  name: documentAmount
  type: number
- description: ''
  name: currencyCode
  type: string
- description: ''
  name: errorMessage
  type: string
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/ecommerce-gateway-outbound-transaction-schema.json
slug: ecommerce-gateway-outbound-transaction
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: OutboundTransaction
---
