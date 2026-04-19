---
aid: amazon-athena:amazon-athena-api
baseURL: https://athena.us-east-1.amazonaws.com
description: REST management API for Amazon Athena covering query executions, named queries, work groups, data catalogs, databases, table metadata, and prepared statements.
humanURL: https://docs.aws.amazon.com/athena/latest/APIReference/Welcome.html
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Amazon Athena API
properties:
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/openapi/amazon-athena-openapi.yml
- type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/rules/amazon-athena-spectral-rules.yml
- type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/capabilities/shared/athena-api.yaml
- type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/capabilities/sql-analytics.yaml
- type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/vocabulary/amazon-athena-vocabulary.yaml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/json-schema/athena-query-execution-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/json-schema/athena-named-query-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/json-schema/athena-work-group-schema.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/json-structure/athena-query-execution-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/json-structure/athena-work-group-structure.json
- type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/json-ld/amazon-athena-context.jsonld
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/examples/athena-query-execution-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/amazon-athena/refs/heads/main/examples/athena-named-query-example.json
provider_name: Amazon Athena
provider_slug: amazon-athena
slug: amazon-athena-api
tags:
- Amazon Athena
- SQL
- Analytics
- Serverless
- AWS
---
