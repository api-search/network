---
description: The indexing policy for a container.
layout: schema
name: IndexingPolicy
properties_list:
- description: Whether indexing is automatic.
  name: automatic
  type: boolean
- description: The indexing mode.
  name: indexingMode
  type: string
- description: Paths to include in indexing.
  name: includedPaths
  type: array
- description: Paths to exclude from indexing.
  name: excludedPaths
  type: array
- description: Composite indexes for the container.
  name: compositeIndexes
  type: array
- description: Spatial indexes for the container.
  name: spatialIndexes
  type: array
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-cosmos-db-indexing-policy-schema.json
slug: azure-cosmos-db-indexing-policy
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: IndexingPolicy
---
