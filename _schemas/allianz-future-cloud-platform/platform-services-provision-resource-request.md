---
description: Request body for provisioning an infrastructure resource
layout: schema
name: ProvisionResourceRequest
properties_list:
- description: Type of infrastructure resource to provision
  name: resource_type
  type: string
- description: Name for the infrastructure resource
  name: name
  type: string
- description: Namespace the resource will be associated with
  name: namespace
  type: string
- description: Resource-specific configuration parameters
  name: configuration
  type: object
provider_name: Allianz Future Cloud Platform
provider_slug: allianz-future-cloud-platform
schema_file: json-schema/platform-services-provision-resource-request-schema.json
slug: platform-services-provision-resource-request
tags:
- Cloud Platform
- Enterprise
- Financial Services
- Insurance
- Platform Engineering
- Kubernetes
title: ProvisionResourceRequest
---
