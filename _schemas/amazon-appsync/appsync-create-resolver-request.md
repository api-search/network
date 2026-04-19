---
description: Request to create a resolver
layout: schema
name: CreateResolverRequest
properties_list:
- description: The GraphQL field name
  name: fieldName
  type: string
- description: The data source name
  name: dataSourceName
  type: string
- description: Request mapping template
  name: requestMappingTemplate
  type: string
- description: Response mapping template
  name: responseMappingTemplate
  type: string
- description: Resolver kind
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
- description: Function code for APPSYNC_JS runtime
  name: code
  type: string
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-create-resolver-request-schema.json
slug: appsync-create-resolver-request
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: CreateResolverRequest
---
