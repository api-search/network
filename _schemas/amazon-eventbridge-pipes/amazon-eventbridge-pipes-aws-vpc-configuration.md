---
description: This structure specifies the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the <code>awsvpc</code> network mode.
layout: schema
name: AwsVpcConfiguration
properties_list:
- description: ''
  name: AssignPublicIp
  type: object
- description: ''
  name: SecurityGroups
  type: object
- description: ''
  name: Subnets
  type: object
provider_name: Amazon EventBridge Pipes
provider_slug: amazon-eventbridge-pipes
schema_file: json-schema/amazon-eventbridge-pipes-aws-vpc-configuration-schema.json
slug: amazon-eventbridge-pipes-aws-vpc-configuration
tags:
- Amazon Web Services
- AWS
- Event-Driven
- Integration
- Messaging
- Serverless
title: AwsVpcConfiguration
---
