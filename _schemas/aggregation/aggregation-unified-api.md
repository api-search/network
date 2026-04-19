---
description: Represents a unified API aggregation layer that exposes multiple underlying provider APIs through a single normalized interface.
layout: schema
name: UnifiedAPI
properties_list:
- description: Name of the unified API platform.
  name: name
  type: string
- description: Description of what the unified API covers.
  name: description
  type: string
- description: Business category covered by the unified API.
  name: category
  type: string
- description: List of underlying API providers aggregated by this unified API.
  name: providers
  type: array
- description: Base URL of the unified API.
  name: base_url
  type: string
- description: Authentication mechanism for the unified API.
  name: authentication
  type: object
- description: Whether the API normalizes response schemas across all underlying providers.
  name: normalized_schema
  type: boolean
provider_name: Aggregation
provider_slug: aggregation
schema_file: json-schema/aggregation-unified-api-schema.json
slug: aggregation-unified-api
tags:
- API Aggregation
- API Directory
- API Marketplace
title: UnifiedAPI
---
