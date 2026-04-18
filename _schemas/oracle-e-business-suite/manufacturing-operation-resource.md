---
description: ''
layout: schema
name: OperationResource
properties_list:
- description: Resource sequence number
  name: resourceSeqNum
  type: integer
- description: Resource identifier
  name: resourceId
  type: integer
- description: Resource code
  name: resourceCode
  type: string
- description: Resource usage rate or amount
  name: usageRateOrAmount
  type: number
- description: Basis type (1=Item, 2=Lot, 3=Resource Units, 4=Resource Value)
  name: basisType
  type: integer
- description: Schedule flag
  name: scheduleFlag
  type: integer
- description: Auto-charge type
  name: autochargeType
  type: integer
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/manufacturing-operation-resource-schema.json
slug: manufacturing-operation-resource
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: OperationResource
---
