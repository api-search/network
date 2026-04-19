---
description: Describes an EC2 instance
layout: schema
name: Instance
properties_list:
- description: The ID of the instance
  name: instanceId
  type: string
- description: The ID of the AMI used to launch the instance
  name: imageId
  type: string
- description: The instance type
  name: instanceType
  type: string
- description: The name of the key pair
  name: keyName
  type: string
- description: The time the instance was launched
  name: launchTime
  type: string
- description: The location where the instance launched
  name: placement
  type: object
- description: The monitoring for the instance
  name: monitoring
  type: object
- description: The current state of the instance
  name: instanceState
  type: object
- description: The ID of the subnet in which the instance is running
  name: subnetId
  type: string
- description: The ID of the VPC in which the instance is running
  name: vpcId
  type: string
- description: The private IPv4 address assigned to the instance
  name: privateIpAddress
  type: string
- description: The public IPv4 address assigned to the instance
  name: publicIpAddress
  type: string
- description: The architecture of the image
  name: architecture
  type: string
- description: The root device type used by the AMI
  name: rootDeviceType
  type: string
- description: Any tags assigned to the instance
  name: tags
  type: array
- description: The security groups for the instance
  name: securityGroups
  type: array
provider_name: Amazon EC2
provider_slug: amazon-ec2
schema_file: json-schema/ec2-openapi-instance-schema.json
slug: ec2-openapi-instance
tags:
- AWS
- Cloud Computing
- Compute
- IaaS
- Infrastructure
- Virtual Machines
title: Instance
---
