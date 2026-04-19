---
description: Request body for creating a service.
layout: schema
name: CreateServiceRequest
properties_list:
- description: The name that you want to assign to the service.
  name: Name
  type: string
- description: The ID of the namespace that you want to use to create the service.
  name: NamespaceId
  type: string
- description: A description for the service.
  name: Description
  type: string
- description: A complex type that contains information about the Amazon Route 53 records that you want AWS Cloud Map to create when you register an instance.
  name: DnsConfig
  type: object
- description: A unique string that identifies the request and allows failed CreateService requests to be retried.
  name: CreatorRequestId
  type: string
provider_name: Amazon Cloud Map
provider_slug: amazon-cloud-map
schema_file: json-schema/cloud-map-create-service-request-schema.json
slug: cloud-map-create-service-request
tags:
- AWS
- Cloud Map
- Service Discovery
- Microservices
- DNS
title: CreateServiceRequest
---
