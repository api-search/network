---
description: Use this structure to specify the distribution of On-Demand Instances and Spot Instances and the allocation strategies used to fulfill On-Demand and Spot capacities for a mixed instances policy.
layout: schema
name: InstancesDistribution
properties_list:
- description: ''
  name: OnDemandAllocationStrategy
  type: object
- description: ''
  name: OnDemandBaseCapacity
  type: object
- description: ''
  name: OnDemandPercentageAboveBaseCapacity
  type: object
- description: ''
  name: SpotAllocationStrategy
  type: object
- description: ''
  name: SpotInstancePools
  type: object
- description: ''
  name: SpotMaxPrice
  type: object
provider_name: Amazon EC2 Auto Scaling
provider_slug: amazon-ec2-auto-scaling
schema_file: json-schema/ec2-auto-scaling-instances-distribution-schema.json
slug: ec2-auto-scaling-instances-distribution
tags:
- Amazon Web Services
- Auto Scaling
- AWS
- Compute
- EC2
- High Availability
- Scaling
title: InstancesDistribution
---
