---
description: Describes a load balancer
layout: schema
name: LoadBalancer
properties_list:
- description: The Amazon Resource Name (ARN) of the load balancer
  name: loadBalancerArn
  type: string
- description: The public DNS name of the load balancer
  name: dnsName
  type: string
- description: The ID of the Amazon Route 53 hosted zone for the load balancer
  name: canonicalHostedZoneId
  type: string
- description: The date and time the load balancer was created
  name: createdTime
  type: string
- description: The name of the load balancer
  name: loadBalancerName
  type: string
- description: The scheme of the load balancer
  name: scheme
  type: string
- description: The ID of the VPC for the load balancer
  name: vpcId
  type: string
- description: The state of the load balancer
  name: state
  type: object
- description: The type of load balancer
  name: type
  type: string
- description: The subnets for the load balancer
  name: availabilityZones
  type: array
- description: The IDs of the security groups for the load balancer
  name: securityGroups
  type: array
- description: The type of IP addresses used by the subnets
  name: ipAddressType
  type: string
provider_name: Amazon Elastic Load Balancing
provider_slug: amazon-elastic-load-balancing
schema_file: json-schema/amazon-elastic-load-balancing-load-balancer-schema.json
slug: amazon-elastic-load-balancing-load-balancer
tags:
- Amazon Web Services
- AWS
- High Availability
- Load Balancing
- Networking
- Scalability
title: LoadBalancer
---
