---
description: An API key for AppSync API authentication
layout: schema
name: ApiKey
properties_list:
- description: The API key ID
  name: id
  type: string
- description: The API key description
  name: description
  type: string
- description: Unix timestamp when the key expires
  name: expires
  type: integer
- description: Unix timestamp when the key is scheduled for deletion
  name: deletes
  type: integer
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-api-key-schema.json
slug: appsync-api-key
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: ApiKey
---
