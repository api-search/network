---
description: ''
layout: schema
name: WipOperation
properties_list:
- description: WIP entity identifier
  name: wipEntityId
  type: integer
- description: Operation sequence number
  name: operationSeqNum
  type: integer
- description: Organization identifier
  name: organizationId
  type: integer
- description: Department identifier
  name: departmentId
  type: integer
- description: ''
  name: departmentCode
  type: string
- description: Operation description
  name: operationDescription
  type: string
- description: ''
  name: scheduledQuantity
  type: number
- description: Quantity in queue
  name: quantityInQueue
  type: number
- description: Quantity running
  name: quantityRunning
  type: number
- description: Quantity completed
  name: quantityCompleted
  type: number
- description: Quantity scrapped
  name: quantityScrapped
  type: number
- description: ''
  name: firstUnitStartDate
  type: string
- description: ''
  name: lastUnitCompletionDate
  type: string
- description: ''
  name: countPointType
  type: integer
- description: ''
  name: backflushFlag
  type: integer
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/manufacturing-wip-operation-schema.json
slug: manufacturing-wip-operation
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: WipOperation
---
