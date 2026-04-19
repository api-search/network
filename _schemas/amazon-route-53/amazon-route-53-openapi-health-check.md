---
description: A complex type that contains information about a health check.
layout: schema
name: HealthCheck
properties_list:
- description: The identifier that Amazon Route 53 assigned to the health check.
  name: Id
  type: string
- description: A unique string that you specified when you created the health check.
  name: CallerReference
  type: string
- description: ''
  name: LinkedService
  type: object
- description: Configuration for the health check.
  name: HealthCheckConfig
  type: object
- description: The version of the health check.
  name: HealthCheckVersion
  type: integer
provider_name: Amazon Route 53
provider_slug: amazon-route-53
schema_file: json-schema/amazon-route-53-openapi-health-check-schema.json
slug: amazon-route-53-openapi-health-check
tags:
- AWS
- DNS
- Domain Registration
- Health Checks
- Routing
title: HealthCheck
---
