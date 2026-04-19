---
description: A complex type that contains general information about the hosted zone.
layout: schema
name: HostedZone
properties_list:
- description: The ID that Amazon Route 53 assigned to the hosted zone.
  name: Id
  type: string
- description: The name of the domain. For public hosted zones, this is the name that you registered with your DNS registrar.
  name: Name
  type: string
- description: The value that you specified for CallerReference when you created the hosted zone.
  name: CallerReference
  type: string
- description: ''
  name: Config
  type: object
- description: The number of resource record sets in the hosted zone.
  name: ResourceRecordSetCount
  type: integer
- description: ''
  name: LinkedService
  type: object
provider_name: Amazon Route 53
provider_slug: amazon-route-53
schema_file: json-schema/amazon-route-53-openapi-hosted-zone-schema.json
slug: amazon-route-53-openapi-hosted-zone
tags:
- AWS
- DNS
- Domain Registration
- Health Checks
- Routing
title: HostedZone
---
