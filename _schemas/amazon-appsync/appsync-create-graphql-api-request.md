---
description: Request to create a GraphQL API
layout: schema
name: CreateGraphqlApiRequest
properties_list:
- description: The API name
  name: name
  type: string
- description: Default authentication type
  name: authenticationType
  type: string
- description: logConfig
  name: logConfig
  type: string
- description: Additional authentication providers
  name: additionalAuthenticationProviders
  type: array
- description: Enable X-Ray tracing
  name: xrayEnabled
  type: boolean
- description: Resource tags
  name: tags
  type: object
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
schema_file: json-schema/appsync-create-graphql-api-request-schema.json
slug: appsync-create-graphql-api-request
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: CreateGraphqlApiRequest
---
