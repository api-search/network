---
description: ''
layout: schema
name: RollRequest
properties_list:
- description: Percentage of instances to replace in each batch.
  name: batchSizePercentage
  type: integer
- description: Grace period in seconds before checking health.
  name: gracePeriod
  type: integer
- description: ''
  name: healthCheckType
  type: string
provider_name: Spot
provider_slug: spot
schema_file: json-schema/spot-elastigroup-roll-request-schema.json
slug: spot-elastigroup-roll-request
tags:
- Autoscaling
- Cloud Infrastructure
- Containers
- Cost Optimization
- FinOps
- Kubernetes
- Spot Instances
title: RollRequest
---
