---
description: SignedUrl schema from Ampersand API
layout: schema
name: SignedUrl
properties_list:
- description: The signed URL to upload the zip file to.
  name: url
  type: string
- description: The bucket (will match the bucket part of the url).
  name: bucket
  type: string
- description: The path (will match the path part of the url).
  name: path
  type: string
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-signed-url-schema.json
slug: ampersand-api-signed-url
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: SignedUrl
---
