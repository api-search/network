---
description: Specifies the configuration for the domain cluster, such as the type and number of instances.
layout: schema
name: ElasticsearchClusterConfig
properties_list:
- description: ''
  name: InstanceType
  type: object
- description: ''
  name: InstanceCount
  type: object
- description: ''
  name: DedicatedMasterEnabled
  type: object
- description: ''
  name: ZoneAwarenessEnabled
  type: object
- description: ''
  name: ZoneAwarenessConfig
  type: object
- description: ''
  name: DedicatedMasterType
  type: object
- description: ''
  name: DedicatedMasterCount
  type: object
- description: ''
  name: WarmEnabled
  type: object
- description: ''
  name: WarmType
  type: object
- description: ''
  name: WarmCount
  type: object
- description: ''
  name: ColdStorageOptions
  type: object
provider_name: Amazon OpenSearch Service API
provider_slug: amazon-opensearch
schema_file: json-schema/openapi-elasticsearch-cluster-config-schema.json
slug: openapi-elasticsearch-cluster-config
tags:
- Analytics
- AWS
- Elasticsearch
- Search
title: ElasticsearchClusterConfig
---
