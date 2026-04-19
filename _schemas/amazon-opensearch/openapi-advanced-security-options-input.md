---
description: 'Specifies the advanced security configuration: whether advanced security is enabled, whether the internal database option is enabled, master username and password (if internal database is enabled), and master user ARN (if IAM is enabled).'
layout: schema
name: AdvancedSecurityOptionsInput
properties_list:
- description: ''
  name: Enabled
  type: object
- description: ''
  name: InternalUserDatabaseEnabled
  type: object
- description: ''
  name: MasterUserOptions
  type: object
- description: ''
  name: SAMLOptions
  type: object
- description: ''
  name: AnonymousAuthEnabled
  type: object
provider_name: Amazon OpenSearch Service API
provider_slug: amazon-opensearch
schema_file: json-schema/openapi-advanced-security-options-input-schema.json
slug: openapi-advanced-security-options-input
tags:
- Analytics
- AWS
- Elasticsearch
- Search
title: AdvancedSecurityOptionsInput
---
