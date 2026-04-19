---
description: Amazon Cognito user pools configuration
layout: schema
name: CognitoUserPoolConfig
properties_list:
- description: User pool ID
  name: userPoolId
  type: string
- description: AWS Region where the user pool exists
  name: awsRegion
  type: string
- description: Regex for client IDs
  name: appIdClientRegex
  type: string
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-cognito-user-pool-config-schema.json
slug: appsync-cognito-user-pool-config
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: CognitoUserPoolConfig
---
