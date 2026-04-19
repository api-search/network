---
description: An association between a custom domain name and a GraphQL API
layout: schema
name: ApiAssociation
properties_list:
- description: The custom domain name
  name: domainName
  type: string
- description: The API ID
  name: apiId
  type: string
- description: The association status
  name: associationStatus
  type: string
- description: Details about the deployment
  name: deploymentDetail
  type: string
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-api-association-schema.json
slug: appsync-api-association
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: ApiAssociation
---
