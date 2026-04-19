---
description: Represents a Cloud Map service used for service discovery.
layout: schema
name: Service
properties_list:
- description: The ID of the service.
  name: Id
  type: string
- description: The Amazon Resource Name (ARN) of the service.
  name: Arn
  type: string
- description: The name of the service.
  name: Name
  type: string
- description: The ID of the namespace.
  name: NamespaceId
  type: string
- description: The description of the service.
  name: Description
  type: string
- description: The number of instances that are currently associated with the service.
  name: InstanceCount
  type: integer
provider_name: Amazon Cloud Map
provider_slug: amazon-cloud-map
schema_file: json-schema/cloud-map-service-schema.json
slug: cloud-map-service
tags:
- AWS
- Cloud Map
- Service Discovery
- Microservices
- DNS
title: Service
---
