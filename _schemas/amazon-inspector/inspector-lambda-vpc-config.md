---
description: The VPC security groups and subnets that are attached to an AWS Lambda function. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html">VPC Settings</a>.
layout: schema
name: LambdaVpcConfig
properties_list:
- description: ''
  name: securityGroupIds
  type: object
- description: ''
  name: subnetIds
  type: object
- description: ''
  name: vpcId
  type: object
provider_name: Amazon Inspector
provider_slug: amazon-inspector
schema_file: json-schema/inspector-lambda-vpc-config-schema.json
slug: inspector-lambda-vpc-config
tags:
- AWS
- Compliance
- Container Security
- EC2
- Lambda
- Security
- Vulnerability Scanning
title: LambdaVpcConfig
---
