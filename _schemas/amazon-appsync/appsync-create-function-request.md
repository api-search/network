---
description: Request to create a pipeline function
layout: schema
name: CreateFunctionRequest
properties_list:
- description: The function name
  name: name
  type: string
- description: Function description
  name: description
  type: string
- description: Data source name
  name: dataSourceName
  type: string
- description: Request mapping template
  name: requestMappingTemplate
  type: string
- description: Response mapping template
  name: responseMappingTemplate
  type: string
- description: Function version
  name: functionVersion
  type: string
- description: syncConfig
  name: syncConfig
  type: string
- description: Maximum batch size
  name: maxBatchSize
  type: integer
- description: runtime
  name: runtime
  type: string
- description: Function code
  name: code
  type: string
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-create-function-request-schema.json
slug: appsync-create-function-request
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: CreateFunctionRequest
---
