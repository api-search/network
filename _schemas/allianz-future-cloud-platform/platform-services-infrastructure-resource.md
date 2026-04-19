---
description: A provisioned cloud infrastructure resource
layout: schema
name: InfrastructureResource
properties_list:
- description: Unique identifier for the resource
  name: resource_id
  type: string
- description: Type of infrastructure resource
  name: resource_type
  type: string
- description: Resource name
  name: name
  type: string
- description: Associated Kubernetes namespace
  name: namespace
  type: string
- description: Provisioning status
  name: status
  type: string
- description: Timestamp when provisioning was initiated
  name: created_at
  type: string
provider_name: Allianz Future Cloud Platform
provider_slug: allianz-future-cloud-platform
schema_file: json-schema/platform-services-infrastructure-resource-schema.json
slug: platform-services-infrastructure-resource
tags:
- Cloud Platform
- Enterprise
- Financial Services
- Insurance
- Platform Engineering
- Kubernetes
title: InfrastructureResource
---
