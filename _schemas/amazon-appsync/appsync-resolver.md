---
description: A resolver for a GraphQL field
layout: schema
name: Resolver
properties_list:
- description: The GraphQL type name
  name: typeName
  type: string
- description: The GraphQL field name
  name: fieldName
  type: string
- description: The data source name
  name: dataSourceName
  type: string
- description: The resolver ARN
  name: resolverArn
  type: string
- description: The request mapping template
  name: requestMappingTemplate
  type: string
- description: The response mapping template
  name: responseMappingTemplate
  type: string
- description: The resolver kind
  name: kind
  type: string
- description: pipelineConfig
  name: pipelineConfig
  type: string
- description: syncConfig
  name: syncConfig
  type: string
- description: cachingConfig
  name: cachingConfig
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
schema_file: json-schema/appsync-resolver-schema.json
slug: appsync-resolver
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: Resolver
---
