---
description: A Kubernetes namespace managed on the platform
layout: schema
name: Namespace
properties_list:
- description: Unique identifier for the namespace
  name: namespace_id
  type: string
- description: Kubernetes namespace name
  name: name
  type: string
- description: Team owning this namespace
  name: team
  type: string
- description: Number of services in this namespace
  name: service_count
  type: integer
- description: Namespace status
  name: status
  type: string
provider_name: Allianz Future Cloud Platform
provider_slug: allianz-future-cloud-platform
schema_file: json-schema/platform-services-namespace-schema.json
slug: platform-services-namespace
tags:
- Cloud Platform
- Enterprise
- Financial Services
- Insurance
- Platform Engineering
- Kubernetes
title: Namespace
---
