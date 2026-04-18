---
description: ''
layout: schema
name: Requisition
properties_list:
- description: Requisition header identifier
  name: requisitionHeaderId
  type: integer
- description: Requisition number
  name: segment1
  type: string
- description: Requisition type
  name: typeLookupCode
  type: string
- description: Authorization status
  name: authorizationStatus
  type: string
- description: Preparer identifier
  name: preparerId
  type: integer
- description: Requisition description
  name: description
  type: string
- description: ''
  name: totalAmount
  type: number
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lines
  type: array
- description: ''
  name: orgId
  type: integer
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/supply-chain-requisition-schema.json
slug: supply-chain-requisition
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: Requisition
---
