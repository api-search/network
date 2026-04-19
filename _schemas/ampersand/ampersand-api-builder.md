---
description: Builder schema from Ampersand API
layout: schema
name: Builder
properties_list:
- description: The builder ID.
  name: id
  type: string
- description: The identity provider
  name: idpProvider
  type: string
- description: ID used by the identity provider
  name: idpRef
  type: string
- description: The time that the builder joined Ampersand.
  name: createTime
  type: string
- description: ''
  name: firstName
  type: string
- description: ''
  name: lastName
  type: string
- description: ''
  name: fullName
  type: string
- description: ''
  name: primaryEmail
  type: string
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-builder-schema.json
slug: ampersand-api-builder
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: Builder
---
