---
description: Schema defining the structure of an Amazon AppSync GraphQL API resource, including authentication configuration, data sources, resolvers, types, and API settings.
layout: schema
name: Amazon AppSync GraphQL API
properties_list:
- description: The unique identifier for the GraphQL API.
  name: apiId
  type: string
- description: The name of the GraphQL API.
  name: name
  type: string
- description: The authentication type for the GraphQL API.
  name: authenticationType
  type: string
- description: The ARN of the GraphQL API.
  name: arn
  type: string
- description: The URIs associated with the GraphQL API.
  name: uris
  type: object
- description: ''
  name: logConfig
  type: object
- description: ''
  name: userPoolConfig
  type: object
- description: ''
  name: openIDConnectConfig
  type: object
- description: ''
  name: lambdaAuthorizerConfig
  type: object
- description: A list of additional authentication providers for the GraphQL API.
  name: additionalAuthenticationProviders
  type: array
- description: Whether AWS X-Ray tracing is enabled for this API.
  name: xrayEnabled
  type: boolean
- description: The ARN of the AWS WAF web ACL associated with this API.
  name: wafWebAclArn
  type: string
- description: Tags for the GraphQL API.
  name: tags
  type: object
- description: The data sources configured for the GraphQL API.
  name: dataSources
  type: array
- description: The resolvers configured for the GraphQL API.
  name: resolvers
  type: array
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/amazon-appsync-schema.json
slug: amazon-appsync
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: Amazon AppSync GraphQL API
---
