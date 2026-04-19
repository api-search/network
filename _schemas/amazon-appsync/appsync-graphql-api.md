---
description: A GraphQL API object managed by AppSync
layout: schema
name: GraphqlApi
properties_list:
- description: The API ID
  name: apiId
  type: string
- description: The API name
  name: name
  type: string
- description: The default authentication type
  name: authenticationType
  type: string
- description: The ARN of the API
  name: arn
  type: string
- description: The URIs for the API endpoint
  name: uris
  type: object
- description: Tags on the API
  name: tags
  type: object
- description: Additional authentication providers
  name: additionalAuthenticationProviders
  type: array
- description: logConfig
  name: logConfig
  type: string
- description: Whether X-Ray tracing is enabled
  name: xrayEnabled
  type: boolean
- description: WAF Web ACL ARN
  name: wafWebAclArn
  type: string
- description: lambdaAuthorizerConfig
  name: lambdaAuthorizerConfig
  type: string
- description: API visibility
  name: visibility
  type: string
- description: API type
  name: apiType
  type: string
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-graphql-api-schema.json
slug: appsync-graphql-api
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: GraphqlApi
---
