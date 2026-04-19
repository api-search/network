---
description: A JSON Schema representation of an Amazon Route 53 hosted zone, which is a container for records that define how to route traffic for a domain and its subdomains.
layout: schema
name: Amazon Route 53 Hosted Zone
properties_list:
- description: The ID that Amazon Route 53 assigned to the hosted zone when it was created.
  name: Id
  type: string
- description: The name of the domain. For public hosted zones, this is the name that you registered with your DNS registrar.
  name: Name
  type: string
- description: The value that you specified for CallerReference when you created the hosted zone.
  name: CallerReference
  type: string
- description: A complex type that includes the Comment and PrivateZone elements.
  name: Config
  type: object
- description: The number of resource record sets in the hosted zone.
  name: ResourceRecordSetCount
  type: integer
- description: If the hosted zone was created by another service, the service that created the hosted zone.
  name: LinkedService
  type: object
- description: The name servers that are associated with the hosted zone.
  name: DelegationSet
  type: object
- description: A list of VPCs associated with a private hosted zone.
  name: VPCs
  type: array
provider_name: Amazon Route 53
provider_slug: amazon-route-53
schema_file: json-schema/amazon-route-53-hosted-zone-schema.json
slug: amazon-route-53-hosted-zone
tags:
- AWS
- DNS
- Domain Registration
- Health Checks
- Routing
title: Amazon Route 53 Hosted Zone
---
