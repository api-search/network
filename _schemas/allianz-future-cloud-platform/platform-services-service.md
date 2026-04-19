---
description: A microservice registered on the Allianz Future Cloud Platform
layout: schema
name: Service
properties_list:
- description: Unique identifier for the service
  name: service_id
  type: string
- description: Kebab-case service name
  name: name
  type: string
- description: Kubernetes namespace the service belongs to
  name: namespace
  type: string
- description: Current operational status
  name: status
  type: string
- description: Number of running pod replicas
  name: replicas
  type: integer
- description: Currently deployed version
  name: version
  type: string
- description: Primary programming language
  name: language
  type: string
- description: Git repository URL
  name: repository_url
  type: string
- description: Timestamp when the service was registered
  name: created_at
  type: string
- description: Timestamp when the service was last updated
  name: modified_at
  type: string
provider_name: Allianz Future Cloud Platform
provider_slug: allianz-future-cloud-platform
schema_file: json-schema/platform-services-service-schema.json
slug: platform-services-service
tags:
- Cloud Platform
- Enterprise
- Financial Services
- Insurance
- Platform Engineering
- Kubernetes
title: Service
---
