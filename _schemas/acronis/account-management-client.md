---
description: OAuth2 client credential
layout: schema
name: Client
properties_list:
- description: OAuth2 client identifier
  name: client_id
  type: string
- description: OAuth2 client secret (only shown on creation)
  name: client_secret
  type: string
- description: Tenant the client belongs to
  name: tenant_id
  type: string
- description: Client type
  name: type
  type: string
- description: ''
  name: status
  type: string
- description: Additional client metadata
  name: data
  type: object
provider_name: Acronis
provider_slug: acronis
schema_file: json-schema/account-management-client-schema.json
slug: account-management-client
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
title: Client
---
