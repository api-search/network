---
description: Configuration for a custom domain name
layout: schema
name: DomainNameConfig
properties_list:
- description: The custom domain name
  name: domainName
  type: string
- description: Domain name description
  name: description
  type: string
- description: ACM certificate ARN
  name: certificateArn
  type: string
- description: AppSync CNAME for DNS setup
  name: appsyncDomainName
  type: string
- description: Route 53 hosted zone ID
  name: hostedZoneId
  type: string
provider_name: Amazon AppSync
provider_slug: amazon-appsync
schema_file: json-schema/appsync-domain-name-config-schema.json
slug: appsync-domain-name-config
tags:
- Amazon AppSync
- GraphQL
- API Management
- Serverless
- AWS
title: DomainNameConfig
---
