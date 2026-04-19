---
description: Request to update a function
layout: schema
name: UpdateFunctionRequest
properties_list:
- description: Function name
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
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-update-function-request-schema.json
slug: appsync-update-function-request
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: UpdateFunctionRequest
---
