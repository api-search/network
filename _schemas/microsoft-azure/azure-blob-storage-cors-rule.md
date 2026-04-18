---
description: CORS rule for the Blob service.
layout: schema
name: CorsRule
properties_list:
- description: Comma-separated list of origin domains that are allowed via CORS.
  name: AllowedOrigins
  type: string
- description: Comma-separated list of HTTP methods that are allowed. Options are DELETE, GET, HEAD, MERGE, POST, OPTIONS, PUT.
  name: AllowedMethods
  type: string
- description: Comma-separated list of headers allowed to be part of the cross-origin request.
  name: AllowedHeaders
  type: string
- description: Comma-separated list of response headers to expose to CORS clients.
  name: ExposedHeaders
  type: string
- description: The maximum amount of time in seconds that a browser should cache the preflight OPTIONS request.
  name: MaxAgeInSeconds
  type: integer
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-blob-storage-cors-rule-schema.json
slug: azure-blob-storage-cors-rule
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: CorsRule
---
