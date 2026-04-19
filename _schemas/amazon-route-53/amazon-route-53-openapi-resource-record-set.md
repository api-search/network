---
description: Information about the resource record set to create or delete.
layout: schema
name: ResourceRecordSet
properties_list:
- description: The name of the domain for the resource record set.
  name: Name
  type: string
- description: The DNS record type.
  name: Type
  type: string
- description: An identifier that differentiates among multiple resource record sets that have the same combination of name and type.
  name: SetIdentifier
  type: string
- description: The weight for weighted routing, ranging from 0 to 255.
  name: Weight
  type: integer
- description: The Amazon EC2 region for latency-based routing.
  name: Region
  type: string
- description: The failover configuration.
  name: Failover
  type: string
- description: The resource record cache time to live (TTL), in seconds.
  name: TTL
  type: integer
- description: The resource records.
  name: ResourceRecords
  type: array
- description: Alias resource record set information.
  name: AliasTarget
  type: object
- description: The ID of the health check to associate with the record set.
  name: HealthCheckId
  type: string
provider_name: Amazon Route 53
provider_slug: amazon-route-53
schema_file: json-schema/amazon-route-53-openapi-resource-record-set-schema.json
slug: amazon-route-53-openapi-resource-record-set
tags:
- AWS
- DNS
- Domain Registration
- Health Checks
- Routing
title: ResourceRecordSet
---
