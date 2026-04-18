---
description: ''
layout: schema
name: RoutingOperation
properties_list:
- description: Operation sequence identifier
  name: operationSequenceId
  type: integer
- description: Operation sequence number
  name: operationSeqNum
  type: integer
- description: Operation description
  name: operationDescription
  type: string
- description: Standard operation code
  name: operationCode
  type: string
- description: Department identifier
  name: departmentId
  type: integer
- description: Department code
  name: departmentCode
  type: string
- description: ''
  name: effectivityDate
  type: string
- description: ''
  name: disableDate
  type: string
- description: ''
  name: minimumTransferQuantity
  type: number
- description: Count point type (1=Yes, 2=No, 3=Auto-charge)
  name: countPointType
  type: integer
- description: ''
  name: resources
  type: array
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/manufacturing-routing-operation-schema.json
slug: manufacturing-routing-operation
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: RoutingOperation
---
