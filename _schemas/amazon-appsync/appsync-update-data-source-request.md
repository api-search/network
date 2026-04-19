---
description: Request to update a data source
layout: schema
name: UpdateDataSourceRequest
properties_list:
- description: Updated description
  name: description
  type: string
- description: Data source type
  name: type
  type: string
- description: IAM role ARN
  name: serviceRoleArn
  type: string
- description: dynamodbConfig
  name: dynamodbConfig
  type: string
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-update-data-source-request-schema.json
slug: appsync-update-data-source-request
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: UpdateDataSourceRequest
---
