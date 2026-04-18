---
description: ''
layout: schema
name: InboundTransaction
properties_list:
- description: Transaction identifier
  name: transactionId
  type: integer
- description: Inbound transaction type code
  name: transactionType
  type: string
- description: Transaction description
  name: transactionDescription
  type: string
- description: Document standard (X12 or EDIFACT)
  name: documentStandard
  type: string
- description: ASC X12 document number (810, 832, 843, 856, 857)
  name: documentNumber
  type: string
- description: Trading partner identifier
  name: tradingPartnerId
  type: integer
- description: ''
  name: tradingPartnerName
  type: string
- description: ''
  name: tradingPartnerSiteId
  type: integer
- description: Processing status
  name: processStatus
  type: string
- description: Document date
  name: documentDate
  type: string
- description: Document total amount
  name: documentAmount
  type: number
- description: Currency code
  name: currencyCode
  type: string
- description: Error message if processing failed
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
schema_file: json-schema/ecommerce-gateway-inbound-transaction-schema.json
slug: ecommerce-gateway-inbound-transaction
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: InboundTransaction
---
