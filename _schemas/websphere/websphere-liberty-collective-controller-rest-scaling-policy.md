---
description: ''
layout: schema
name: ScalingPolicy
properties_list:
- description: Policy name
  name: name
  type: string
- description: Target cluster
  name: clusterName
  type: string
- description: Whether the policy is active
  name: enabled
  type: boolean
- description: Minimum number of cluster members
  name: minMembers
  type: integer
- description: Maximum number of cluster members
  name: maxMembers
  type: integer
- description: ''
  name: scaleUpTrigger
  type: object
- description: ''
  name: scaleDownTrigger
  type: object
- description: Cooldown period in seconds between scaling events
  name: cooldownPeriod
  type: integer
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-liberty-collective-controller-rest-scaling-policy-schema.json
slug: websphere-liberty-collective-controller-rest-scaling-policy
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: ScalingPolicy
---
