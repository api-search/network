---
description: If your simulation job accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and two subnet IDs.
layout: schema
name: VPCConfig
properties_list:
- description: ''
  name: subnets
  type: object
- description: ''
  name: securityGroups
  type: object
- description: ''
  name: assignPublicIp
  type: object
provider_name: Amazon RoboMaker
provider_slug: amazon-robomaker
schema_file: json-schema/amazon-robomaker-openapi-vpc-config-schema.json
slug: amazon-robomaker-openapi-vpc-config
tags:
- AWS
- Robotics
- Simulation
title: VPCConfig
---
