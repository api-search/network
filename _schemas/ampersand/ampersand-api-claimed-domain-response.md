---
description: ClaimedDomainResponse schema from Ampersand API
layout: schema
name: ClaimedDomainResponse
properties_list:
- description: Unique identifier for the claimed domain
  name: id
  type: string
- description: Type of the parent entity that claimed the domain
  name: parentType
  type: string
- description: ID of the parent entity that claimed the domain
  name: parentId
  type: string
- description: The normalized domain name
  name: domain
  type: string
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-claimed-domain-response-schema.json
slug: ampersand-api-claimed-domain-response
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: ClaimedDomainResponse
---
