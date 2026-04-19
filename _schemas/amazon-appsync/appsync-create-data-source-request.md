---
description: Request to create a data source
layout: schema
name: CreateDataSourceRequest
properties_list:
- description: The data source name
  name: name
  type: string
- description: The data source description
  name: description
  type: string
- description: The data source type
  name: type
  type: string
- description: IAM role ARN for AppSync to assume
  name: serviceRoleArn
  type: string
- description: dynamodbConfig
  name: dynamodbConfig
  type: string
- description: lambdaConfig
  name: lambdaConfig
  type: string
- description: httpConfig
  name: httpConfig
  type: string
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-create-data-source-request-schema.json
slug: appsync-create-data-source-request
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: CreateDataSourceRequest
---
