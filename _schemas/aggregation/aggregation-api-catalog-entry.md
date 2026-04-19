---
description: An entry in an API catalog or directory describing a single API provider.
layout: schema
name: APICatalogEntry
properties_list:
- description: Name of the API.
  name: name
  type: string
- description: Brief description of the API's functionality.
  name: description
  type: string
- description: Company or organization providing the API.
  name: provider
  type: string
- description: Business domain category of the API.
  name: category
  type: string
- description: Base URL of the API.
  name: base_url
  type: string
- description: URL to the API's documentation.
  name: documentation_url
  type: string
- description: URL to an OpenAPI specification for this API.
  name: openapi_url
  type: string
- description: Pricing model for accessing this API.
  name: pricing_model
  type: string
- description: Authentication methods supported by this API.
  name: authentication_types
  type: array
- description: Tags categorizing this API.
  name: tags
  type: array
provider_name: Aggregation
provider_slug: aggregation
schema_file: json-schema/aggregation-api-catalog-entry-schema.json
slug: aggregation-api-catalog-entry
tags:
- API Aggregation
- API Directory
- API Marketplace
title: APICatalogEntry
---
