---
description: Represents an Amazon EC2 virtual server instance with its associated configuration, state, and metadata.
layout: schema
name: Amazon EC2 Instance
properties_list:
- description: The unique identifier for the instance
  name: instanceId
  type: string
- description: The ID of the AMI used to launch the instance
  name: imageId
  type: string
- description: The instance type (e.g., t2.micro, m5.large, c5.xlarge)
  name: instanceType
  type: string
- description: The name of the key pair used for SSH access
  name: keyName
  type: string
- description: The time the instance was launched
  name: launchTime
  type: string
- description: ''
  name: instanceState
  type: object
- description: ''
  name: placement
  type: object
- description: The ID of the subnet the instance is running in
  name: subnetId
  type: string
- description: The ID of the VPC the instance is running in
  name: vpcId
  type: string
- description: The private IPv4 address assigned to the instance
  name: privateIpAddress
  type: string
- description: The public IPv4 address assigned to the instance
  name: publicIpAddress
  type: string
- description: The architecture of the instance
  name: architecture
  type: string
- description: The root device type used by the AMI
  name: rootDeviceType
  type: string
- description: The device name of the root device volume
  name: rootDeviceName
  type: string
- description: Block device mappings for the instance
  name: blockDeviceMappings
  type: array
- description: The security groups associated with the instance
  name: securityGroups
  type: array
- description: Tags assigned to the instance
  name: tags
  type: array
- description: The monitoring state of the instance
  name: monitoring
  type: object
- description: The platform of the instance (Windows or empty for Linux)
  name: platform
  type: string
- description: Indicates whether the instance is optimized for Amazon EBS I/O
  name: ebsOptimized
  type: boolean
- description: Specifies whether enhanced networking with ENA is enabled
  name: enaSupport
  type: boolean
provider_name: Amazon EC2
provider_slug: amazon-ec2
schema_file: json-schema/amazon-ec2-instance-schema.json
slug: amazon-ec2-instance
tags:
- AWS
- Cloud Computing
- Compute
- IaaS
- Infrastructure
- Virtual Machines
title: Amazon EC2 Instance
---
