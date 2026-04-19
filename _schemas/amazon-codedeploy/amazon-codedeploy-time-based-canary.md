---
description: A configuration that shifts traffic from one version of a Lambda function or Amazon ECS task set to another in two increments. The original and target Lambda function versions or ECS task sets are specified in the deployment's AppSpec file.
layout: schema
name: TimeBasedCanary
properties_list:
- description: ''
  name: canaryPercentage
  type: object
- description: ''
  name: canaryInterval
  type: object
provider_name: Amazon CodeDeploy
provider_slug: amazon-codedeploy
schema_file: json-schema/amazon-codedeploy-time-based-canary-schema.json
slug: amazon-codedeploy-time-based-canary
tags:
- Amazon
- AWS
- Deployment
- DevOps
- CI/CD
- Release Management
- Blue/Green Deployment
title: TimeBasedCanary
---
