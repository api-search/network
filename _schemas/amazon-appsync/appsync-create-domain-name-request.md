---
description: Request to create a custom domain name
layout: schema
name: CreateDomainNameRequest
properties_list:
- description: The custom domain name
  name: domainName
  type: string
- description: ACM certificate ARN
  name: certificateArn
  type: string
- description: Domain name description
  name: description
  type: string
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-create-domain-name-request-schema.json
slug: appsync-create-domain-name-request
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: CreateDomainNameRequest
---
