---
description: Request to update a resolver
layout: schema
name: UpdateResolverRequest
properties_list:
- description: Data source name
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
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-update-resolver-request-schema.json
slug: appsync-update-resolver-request
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: UpdateResolverRequest
---
