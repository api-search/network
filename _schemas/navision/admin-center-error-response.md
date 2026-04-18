---
description: ''
layout: schema
name: ErrorResponse
properties_list:
- description: A stable error code describing the type and nature of the error
  name: code
  type: string
- description: A readable description of the error and cause
  name: message
  type: string
- description: Information about what part of the request caused the error
  name: target
  type: string
- description: Additional key/value information about the error
  name: extensionData
  type: object
- description: Nested list of error objects with more details
  name: clientError
  type: array
provider_name: Microsoft Dynamics NAV
provider_slug: navision
schema_file: json-schema/admin-center-error-response-schema.json
slug: admin-center-error-response
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
title: ErrorResponse
---
