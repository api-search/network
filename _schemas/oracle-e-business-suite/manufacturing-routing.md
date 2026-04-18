---
description: ''
layout: schema
name: Routing
properties_list:
- description: Routing sequence identifier
  name: routingSequenceId
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
- description: Alternate routing designator
  name: alternateDesignator
  type: string
- description: Routing type (1=Manufacturing, 2=Engineering)
  name: routingType
  type: integer
- description: ''
  name: operations
  type: array
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/manufacturing-routing-schema.json
slug: manufacturing-routing
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: Routing
---
