---
description: Client information mapping with source system identifiers
layout: schema
name: SourceSystemClientMapping
properties_list:
- description: Source system Client unique ID created and managed by institution system. <BR/> This field is required if configured as **Business Mandatory**<font color='red'>* </font>.
  name: clientId
  type: string
- description: Client unique Reference Number created and managed by institution CBS. <BR/> This field is required if configured as **Business Mandatory**<font color='red'>* </font>.
  name: cbsReferenceNumber
  type: string
- description: Client unique ID created and managed by institution CBS.
  name: cbsClientId
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-source-system-client-mapping-schema.json
slug: mastercard-card-issuance-source-system-client-mapping
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: SourceSystemClientMapping
---
