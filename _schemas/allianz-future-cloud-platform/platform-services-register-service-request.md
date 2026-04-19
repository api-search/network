---
description: Request body for registering a new service
layout: schema
name: RegisterServiceRequest
properties_list:
- description: Kebab-case service name
  name: name
  type: string
- description: Target Kubernetes namespace
  name: namespace
  type: string
- description: Primary programming language
  name: language
  type: string
- description: Git repository URL for the service
  name: repository_url
  type: string
- description: ''
  name: resource_requirements
  type: object
provider_name: Allianz Future Cloud Platform
provider_slug: allianz-future-cloud-platform
schema_file: json-schema/platform-services-register-service-request-schema.json
slug: platform-services-register-service-request
tags:
- Cloud Platform
- Enterprise
- Financial Services
- Insurance
- Platform Engineering
- Kubernetes
title: RegisterServiceRequest
---
