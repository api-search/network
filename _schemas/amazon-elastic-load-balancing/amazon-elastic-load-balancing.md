---
description: Represents an Amazon Elastic Load Balancer with its associated configuration, state, listeners, and target groups.
layout: schema
name: Amazon Elastic Load Balancer
properties_list:
- description: The Amazon Resource Name (ARN) of the load balancer
  name: loadBalancerArn
  type: string
- description: The name of the load balancer
  name: loadBalancerName
  type: string
- description: The public DNS name of the load balancer
  name: dnsName
  type: string
- description: The ID of the Amazon Route 53 hosted zone associated with the load balancer
  name: canonicalHostedZoneId
  type: string
- description: The date and time the load balancer was created
  name: createdTime
  type: string
- description: The scheme of the load balancer (internet-facing or internal)
  name: scheme
  type: string
- description: The ID of the VPC for the load balancer
  name: vpcId
  type: string
- description: ''
  name: state
  type: object
- description: The type of load balancer
  name: type
  type: string
- description: The Availability Zones for the load balancer
  name: availabilityZones
  type: array
- description: The IDs of the security groups for the load balancer
  name: securityGroups
  type: array
- description: The type of IP addresses used by the subnets for the load balancer
  name: ipAddressType
  type: string
- description: The ID of the customer-owned address pool
  name: customerOwnedIpv4Pool
  type: string
- description: The listeners configured for the load balancer
  name: listeners
  type: array
- description: The target groups associated with the load balancer
  name: targetGroups
  type: array
- description: Tags assigned to the load balancer
  name: tags
  type: array
provider_name: Amazon Elastic Load Balancing
provider_slug: amazon-elastic-load-balancing
schema_file: json-schema/amazon-elastic-load-balancing-schema.json
slug: amazon-elastic-load-balancing
tags:
- Amazon Web Services
- AWS
- High Availability
- Load Balancing
- Networking
- Scalability
title: Amazon Elastic Load Balancer
---
