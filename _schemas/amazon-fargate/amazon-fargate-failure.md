---
description: A failure returned by an API operation
layout: schema
name: Failure
properties_list:
- description: ARN of the resource that failed
  name: arn
  type: string
- description: Reason for the failure
  name: reason
  type: string
- description: Additional detail about the failure
  name: detail
  type: string
provider_name: Amazon Fargate
provider_slug: amazon-fargate
schema_file: json-schema/amazon-fargate-failure-schema.json
slug: amazon-fargate-failure
tags:
- AWS
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
title: Failure
---
