---
description: ''
layout: schema
name: InboundTransactionImport
properties_list:
- description: Inbound transaction type
  name: transactionType
  type: string
- description: ''
  name: tradingPartnerId
  type: integer
- description: ''
  name: tradingPartnerSiteId
  type: integer
- description: ''
  name: documentDate
  type: string
- description: Transaction-specific document data. Structure varies by transaction type (invoice, ship notice, etc.)
  name: documentData
  type: object
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/ecommerce-gateway-inbound-transaction-import-schema.json
slug: ecommerce-gateway-inbound-transaction-import
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: InboundTransactionImport
---
