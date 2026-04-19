---
description: VPC connectivity settings for a Lambda function
layout: schema
name: VpcConfig
properties_list:
- description: A list of VPC subnet IDs
  name: SubnetIds
  type: array
- description: A list of VPC security group IDs
  name: SecurityGroupIds
  type: array
provider_name: AWS Lambda
provider_slug: aws-lambda
schema_file: json-schema/aws-lambda-vpc-config-schema.json
slug: aws-lambda-vpc-config
tags: []
title: VpcConfig
---
