---
description: A data source configuration for a GraphQL API
layout: schema
name: DataSource
properties_list:
- description: The ARN of the data source
  name: dataSourceArn
  type: string
- description: The data source name
  name: name
  type: string
- description: The data source description
  name: description
  type: string
- description: The data source type
  name: type
  type: string
- description: IAM service role ARN
  name: serviceRoleArn
  type: string
- description: dynamodbConfig
  name: dynamodbConfig
  type: string
- description: lambdaConfig
  name: lambdaConfig
  type: string
- description: elasticsearchConfig
  name: elasticsearchConfig
  type: string
- description: httpConfig
  name: httpConfig
  type: string
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-data-source-schema.json
slug: appsync-data-source
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: DataSource
---
