---
aid: amazon-aurora-dsql:amazon-aurora-dsql-api
baseURL: https://dsql.us-east-1.amazonaws.com
description: REST management API for Amazon Aurora DSQL covering cluster creation, configuration, multi-region deployments, and connection endpoint management.
humanURL: https://docs.aws.amazon.com/aurora-dsql/latest/userguide/getting-started.html
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Amazon Aurora DSQL API
properties:
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/openapi/amazon-aurora-dsql-openapi.yml
- type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/rules/amazon-aurora-dsql-spectral-rules.yml
- type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/capabilities/shared/aurora-dsql-api.yaml
- type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/capabilities/distributed-sql-management.yaml
- type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/vocabulary/amazon-aurora-dsql-vocabulary.yaml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/json-schema/aurora-dsql-cluster-summary-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/json-schema/aurora-dsql-create-cluster-input-schema.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/json-structure/aurora-dsql-cluster-summary-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/json-structure/aurora-dsql-get-cluster-output-structure.json
- type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/json-ld/amazon-aurora-dsql-context.jsonld
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/examples/aurora-dsql-create-cluster-input-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora-dsql/refs/heads/main/examples/aurora-dsql-get-cluster-output-example.json
provider_name: Amazon Aurora DSQL
provider_slug: amazon-aurora-dsql
slug: amazon-aurora-dsql-api
tags:
- Amazon Aurora DSQL
- Distributed SQL
- PostgreSQL
- Serverless
- AWS
---
