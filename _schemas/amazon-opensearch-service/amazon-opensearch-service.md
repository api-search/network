---
description: Schema defining the structure of an Amazon OpenSearch Service domain resource, including cluster configuration, storage options, access policies, encryption settings, and VPC configuration.
layout: schema
name: Amazon OpenSearch Service Domain Definition
properties_list:
- description: The unique identifier for the OpenSearch domain.
  name: DomainId
  type: string
- description: The name of the OpenSearch domain.
  name: DomainName
  type: string
- description: The Amazon Resource Name of the domain.
  name: ARN
  type: string
- description: Whether the domain creation is complete.
  name: Created
  type: boolean
- description: Whether the domain is being deleted.
  name: Deleted
  type: boolean
- description: The domain endpoint used to submit index, search, and data upload requests.
  name: Endpoint
  type: string
- description: Map of VPC endpoints for the domain.
  name: Endpoints
  type: object
- description: The version of OpenSearch or Elasticsearch running on the domain.
  name: EngineVersion
  type: string
- description: ''
  name: ClusterConfig
  type: object
- description: ''
  name: EBSOptions
  type: object
- description: IAM access policy as a JSON-formatted string.
  name: AccessPolicies
  type: string
- description: ''
  name: SnapshotOptions
  type: object
- description: ''
  name: VPCOptions
  type: object
- description: ''
  name: EncryptionAtRestOptions
  type: object
- description: ''
  name: NodeToNodeEncryptionOptions
  type: object
- description: Key-value pairs for advanced configuration options.
  name: AdvancedOptions
  type: object
- description: Log publishing options for the domain.
  name: LogPublishingOptions
  type: object
- description: ''
  name: DomainEndpointOptions
  type: object
- description: ''
  name: AutoTuneOptions
  type: object
- description: Tags associated with the domain.
  name: tags
  type: array
provider_name: Amazon OpenSearch Service
provider_slug: amazon-opensearch-service
schema_file: json-schema/amazon-opensearch-service-schema.json
slug: amazon-opensearch-service
tags:
- Analytics
- AWS
- Elasticsearch
- Full-Text Search
- Log Analytics
- OpenSearch
- Search
title: Amazon OpenSearch Service Domain Definition
---
