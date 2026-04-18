---
description: ''
layout: schema
name: EnvironmentOperation
properties_list:
- description: Operation ID used for tracking
  name: id
  type: string
- description: Type of operation
  name: type
  type: string
- description: Status of the operation
  name: status
  type: string
- description: Microsoft Entra tenant ID
  name: aadTenantId
  type: string
- description: When the operation was created
  name: createdOn
  type: string
- description: When the operation started executing
  name: startedOn
  type: string
- description: When the operation completed
  name: completedOn
  type: string
- description: Who created the operation
  name: createdBy
  type: string
- description: Error message for failed operations
  name: errorMessage
  type: string
- description: Operation-specific parameters
  name: parameters
  type: object
- description: Name of the affected environment
  name: environmentName
  type: string
- description: Type of the affected environment
  name: environmentType
  type: string
- description: Product family of the affected environment
  name: productFamily
  type: string
provider_name: Microsoft Dynamics NAV
provider_slug: navision
schema_file: json-schema/admin-center-environment-operation-schema.json
slug: admin-center-environment-operation
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
title: EnvironmentOperation
---
