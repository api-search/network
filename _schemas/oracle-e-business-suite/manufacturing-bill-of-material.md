---
description: ''
layout: schema
name: BillOfMaterial
properties_list:
- description: Bill sequence identifier
  name: billSequenceId
  type: integer
- description: Assembly item identifier
  name: assemblyItemId
  type: integer
- description: Assembly item number
  name: assemblyItemNumber
  type: string
- description: Organization identifier
  name: organizationId
  type: integer
- description: Alternate BOM designator
  name: alternateDesignator
  type: string
- description: Assembly type (1=Manufacturing, 2=Engineering)
  name: assemblyType
  type: integer
- description: Common bill sequence identifier
  name: commonBillSequenceId
  type: integer
- description: Assembly comment
  name: specificAssemblyComment
  type: string
- description: ''
  name: components
  type: array
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/manufacturing-bill-of-material-schema.json
slug: manufacturing-bill-of-material
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: BillOfMaterial
---
