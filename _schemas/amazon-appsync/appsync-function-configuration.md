---
description: A reusable pipeline function configuration
layout: schema
name: FunctionConfiguration
properties_list:
- description: The function ID
  name: functionId
  type: string
- description: The function ARN
  name: functionArn
  type: string
- description: The function name
  name: name
  type: string
- description: The function description
  name: description
  type: string
- description: The data source name
  name: dataSourceName
  type: string
- description: The request mapping template
  name: requestMappingTemplate
  type: string
- description: The response mapping template
  name: responseMappingTemplate
  type: string
- description: The function version
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
- description: The function code
  name: code
  type: string
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-function-configuration-schema.json
slug: appsync-function-configuration
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: FunctionConfiguration
---
