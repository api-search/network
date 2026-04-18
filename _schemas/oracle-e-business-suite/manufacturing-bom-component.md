---
description: ''
layout: schema
name: BomComponent
properties_list:
- description: Component sequence identifier
  name: componentSequenceId
  type: integer
- description: Component item identifier
  name: componentItemId
  type: integer
- description: Component item number
  name: componentItemNumber
  type: string
- description: Component item description
  name: itemDescription
  type: string
- description: Operation sequence number where component is consumed
  name: operationSeqNum
  type: integer
- description: Component quantity per assembly
  name: componentQuantity
  type: number
- description: Component yield factor
  name: componentYieldFactor
  type: number
- description: Effective date
  name: effectivityDate
  type: string
- description: Disable date
  name: disableDate
  type: string
- description: WIP supply type (1=Push, 2=Assembly Pull, 3=Operation Pull, 4=Bulk, 5=Supplier, 6=Phantom)
  name: wipSupplyType
  type: integer
- description: Optional flag (1=Yes, 2=No)
  name: optional
  type: integer
- description: Quantity related flag
  name: quantityRelated
  type: integer
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/manufacturing-bom-component-schema.json
slug: manufacturing-bom-component
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: BomComponent
---
