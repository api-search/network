---
description: Represents a summary of a discovered service instance.
layout: schema
name: HttpInstanceSummary
properties_list:
- description: The ID of an instance.
  name: InstanceId
  type: string
- description: The HttpName name of the namespace.
  name: NamespaceName
  type: string
- description: The name of the service.
  name: ServiceName
  type: string
- description: If you configured health checking in the service, the current health status of the service's instances.
  name: HealthStatus
  type: string
- description: Custom attributes associated with the instance.
  name: Attributes
  type: object
provider_name: Amazon Cloud Map
provider_slug: amazon-cloud-map
schema_file: json-schema/cloud-map-http-instance-summary-schema.json
slug: cloud-map-http-instance-summary
tags:
- AWS
- Cloud Map
- Service Discovery
- Microservices
- DNS
title: HttpInstanceSummary
---
