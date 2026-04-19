---
aid: agricultural-statistics-service:quickstats-api
baseURL: https://quickstats.nass.usda.gov/api
description: The QuickStats API provides direct programmatic access to the statistical information contained in the NASS Quick Stats database, covering official published aggregate estimates related to U.S. agricultural production. The API supports filtering by commodity, location, and time with comparison operators. Responses are available in JSON, XML, or CSV format. An API key is required; maximum 50,000 records per request.
humanURL: https://quickstats.nass.usda.gov/api
image: ''
layout: api
name: USDA NASS QuickStats API
properties:
- type: Documentation
  url: https://quickstats.nass.usda.gov/api
- type: APIReference
  url: https://quickstats.nass.usda.gov/api/#param_define
- type: Authentication
  url: https://quickstats.nass.usda.gov/api
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/agricultural-statistics-service/refs/heads/main/openapi/agricultural-statistics-service-quickstats-api.yaml
- title: Statistics Record Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agricultural-statistics-service/refs/heads/main/json-schema/quickstats-api-statistics-record-schema.json
- title: Statistics Response Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agricultural-statistics-service/refs/heads/main/json-schema/quickstats-api-statistics-response-schema.json
- title: Count Response Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agricultural-statistics-service/refs/heads/main/json-schema/quickstats-api-count-response-schema.json
- title: Statistics Record Structure
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/agricultural-statistics-service/refs/heads/main/json-structure/quickstats-api-statistics-record-structure.json
- type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/agricultural-statistics-service/refs/heads/main/json-ld/agricultural-statistics-service-quickstats-api-context.jsonld
provider_name: Agricultural Statistics Service
provider_slug: agricultural-statistics-service
slug: quickstats-api
tags:
- Agricultural Statistics
- Crop Data
- Livestock Data
- Census Of Agriculture
- Open Data
---
