---
description: CreateHostedZoneRequest schema from openapi
layout: schema
name: CreateHostedZoneRequest
properties_list:
- description: The name of the domain.
  name: Name
  type: string
- description: A unique string that identifies the request and allows failed requests to be retried without risk of executing the operation twice.
  name: CallerReference
  type: string
- description: ''
  name: HostedZoneConfig
  type: object
- description: ''
  name: VPC
  type: object
- description: ''
  name: DelegationSetId
  type: string
provider_name: Amazon Route 53
provider_slug: amazon-route-53
schema_file: json-schema/amazon-route-53-openapi-create-hosted-zone-request-schema.json
slug: amazon-route-53-openapi-create-hosted-zone-request
tags:
- AWS
- DNS
- Domain Registration
- Health Checks
- Routing
title: CreateHostedZoneRequest
---
