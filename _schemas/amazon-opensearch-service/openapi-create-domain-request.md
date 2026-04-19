---
description: CreateDomainRequest schema from Amazon OpenSearch Service
layout: schema
name: CreateDomainRequest
properties_list:
- description: Name of the OpenSearch domain to create
  name: DomainName
  type: string
- description: Version of OpenSearch or Elasticsearch
  name: EngineVersion
  type: string
- description: Container for the cluster configuration
  name: ClusterConfig
  type: object
- description: Container for EBS-based storage options
  name: EBSOptions
  type: object
- description: IAM access policy as a JSON-formatted string
  name: AccessPolicies
  type: string
provider_name: Amazon OpenSearch Service
provider_slug: amazon-opensearch-service
schema_file: json-schema/openapi-create-domain-request-schema.json
slug: openapi-create-domain-request
tags:
- Analytics
- AWS
- Elasticsearch
- Full-Text Search
- Log Analytics
- OpenSearch
- Search
title: CreateDomainRequest
---
