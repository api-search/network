---
description: DynamoDB data source configuration
layout: schema
name: DynamodbDataSourceConfig
properties_list:
- description: DynamoDB table name
  name: tableName
  type: string
- description: AWS Region
  name: awsRegion
  type: string
- description: Whether to use caller credentials
  name: useCallerCredentials
  type: boolean
- description: Delta sync configuration
  name: deltaSyncConfig
  type: object
- description: Whether versioning is enabled
  name: versioned
  type: boolean
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-dynamodb-data-source-config-schema.json
slug: appsync-dynamodb-data-source-config
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: DynamodbDataSourceConfig
---
