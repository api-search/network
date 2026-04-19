---
description: Describes a target group
layout: schema
name: TargetGroup
properties_list:
- description: The Amazon Resource Name (ARN) of the target group
  name: targetGroupArn
  type: string
- description: The name of the target group
  name: targetGroupName
  type: string
- description: The protocol to use for routing traffic to the targets
  name: protocol
  type: string
- description: The port on which the targets are listening
  name: port
  type: integer
- description: The ID of the VPC for the targets
  name: vpcId
  type: string
- description: The protocol to use for health checks
  name: healthCheckProtocol
  type: string
- description: The port to use for health checks
  name: healthCheckPort
  type: string
- description: Whether health checks are enabled
  name: healthCheckEnabled
  type: boolean
- description: The approximate interval between health checks
  name: healthCheckIntervalSeconds
  type: integer
- description: The amount of time to wait for a health check response
  name: healthCheckTimeoutSeconds
  type: integer
- description: The number of consecutive health checks required to consider a target healthy
  name: healthyThresholdCount
  type: integer
- description: The number of consecutive health check failures required to consider a target unhealthy
  name: unhealthyThresholdCount
  type: integer
- description: The destination for health checks on the targets
  name: healthCheckPath
  type: string
- description: The type of target
  name: targetType
  type: string
- description: The ARNs of the load balancers that route traffic to this target group
  name: loadBalancerArns
  type: array
provider_name: Amazon Elastic Load Balancing
provider_slug: amazon-elastic-load-balancing
schema_file: json-schema/amazon-elastic-load-balancing-target-group-schema.json
slug: amazon-elastic-load-balancing-target-group
tags:
- Amazon Web Services
- AWS
- High Availability
- Load Balancing
- Networking
- Scalability
title: TargetGroup
---
