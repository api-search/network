---
description: Configuration for Lambda-based authorization
layout: schema
name: LambdaAuthorizerConfig
properties_list:
- description: Lambda function ARN
  name: authorizerUri
  type: string
- description: TTL for authorizer results in seconds
  name: authorizerResultTtlInSeconds
  type: integer
- description: Regular expression for validating tokens
  name: identityValidationExpression
  type: string
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-lambda-authorizer-config-schema.json
slug: appsync-lambda-authorizer-config
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: LambdaAuthorizerConfig
---
