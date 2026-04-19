---
description: Request body for discovering instances.
layout: schema
name: DiscoverInstancesRequest
properties_list:
- description: The HttpName name of the namespace.
  name: NamespaceName
  type: string
- description: The name of the service that you specified when you registered the instance.
  name: ServiceName
  type: string
- description: The maximum number of instances that you want Cloud Map to return.
  name: MaxResults
  type: integer
- description: The health status of the instances that you want to discover.
  name: HealthStatus
  type: string
provider_name: Amazon Cloud Map
provider_slug: amazon-cloud-map
schema_file: json-schema/cloud-map-discover-instances-request-schema.json
slug: cloud-map-discover-instances-request
tags:
- AWS
- Cloud Map
- Service Discovery
- Microservices
- DNS
title: DiscoverInstancesRequest
---
