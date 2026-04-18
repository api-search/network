---
description: The partition key definition.
layout: schema
name: PartitionKeyDefinition
properties_list:
- description: List of paths using which data within the container can be partitioned.
  name: paths
  type: array
- description: The algorithm used for partitioning.
  name: kind
  type: string
- description: The version of the partition key definition.
  name: version
  type: integer
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-cosmos-db-partition-key-definition-schema.json
slug: azure-cosmos-db-partition-key-definition
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: PartitionKeyDefinition
---
