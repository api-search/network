---
description: Metadata pertaining to creation and last modification of the resource.
layout: schema
name: SystemData
properties_list:
- description: The identity that created the resource.
  name: createdBy
  type: string
- description: The type of identity that created the resource.
  name: createdByType
  type: string
- description: The timestamp of resource creation (UTC).
  name: createdAt
  type: string
- description: The identity that last modified the resource.
  name: lastModifiedBy
  type: string
- description: The type of identity that last modified the resource.
  name: lastModifiedByType
  type: string
- description: The timestamp of resource last modification (UTC).
  name: lastModifiedAt
  type: string
provider_name: Azure Kubernetes Service
provider_slug: azure-kubernetes-service
schema_file: json-schema/azure-kubernetes-service-system-data-schema.json
slug: azure-kubernetes-service-system-data
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
title: SystemData
---
