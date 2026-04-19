---
aid: amazon-aurora:amazon-aurora-api
baseURL: https://rds.us-east-1.amazonaws.com
description: REST management API for Amazon Aurora covering DB clusters, DB instances, cluster snapshots, parameter groups, custom endpoints, and global database management.
humanURL: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Amazon Aurora API
properties:
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/openapi/amazon-aurora-openapi.yml
- type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/rules/amazon-aurora-spectral-rules.yml
- type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/capabilities/shared/aurora-api.yaml
- type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/capabilities/relational-database-management.yaml
- type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/vocabulary/amazon-aurora-vocabulary.yaml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/json-schema/aurora-db-cluster-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/json-schema/aurora-create-db-cluster-input-schema.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/json-structure/aurora-db-cluster-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/json-structure/aurora-db-instance-structure.json
- type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/json-ld/amazon-aurora-context.jsonld
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/examples/aurora-db-cluster-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/examples/aurora-create-db-cluster-input-example.json
provider_name: Amazon Aurora
provider_slug: amazon-aurora
slug: amazon-aurora-api
tags:
- Amazon Aurora
- MySQL
- PostgreSQL
- Relational Database
- AWS
---
