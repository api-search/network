---
description: ''
layout: schema
name: CommitmentPlan
properties_list:
- description: The unique identifier of the commitment plan.
  name: id
  type: string
- description: The type of commitment.
  name: type
  type: string
- description: The cloud provider.
  name: provider
  type: string
- description: The current status of the commitment plan.
  name: status
  type: string
- description: The start date of the commitment.
  name: startDate
  type: string
- description: The end date of the commitment.
  name: endDate
  type: string
- description: Estimated monthly savings from this commitment.
  name: monthlySavings
  type: number
- description: Current utilization percentage of the commitment.
  name: utilizationPercentage
  type: number
provider_name: Spot
provider_slug: spot
schema_file: json-schema/spot-eco-commitment-plan-schema.json
slug: spot-eco-commitment-plan
tags:
- Autoscaling
- Cloud Infrastructure
- Containers
- Cost Optimization
- FinOps
- Kubernetes
- Spot Instances
title: CommitmentPlan
---
