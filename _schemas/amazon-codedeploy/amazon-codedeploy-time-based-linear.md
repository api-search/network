---
description: A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in equal increments, with an equal number of minutes between each increment. The original and target Lambda function versions or ECS task sets are specified in the deployment's AppSpec file.
layout: schema
name: TimeBasedLinear
properties_list:
- description: ''
  name: linearPercentage
  type: object
- description: ''
  name: linearInterval
  type: object
provider_name: Amazon CodeDeploy
provider_slug: amazon-codedeploy
schema_file: json-schema/amazon-codedeploy-time-based-linear-schema.json
slug: amazon-codedeploy-time-based-linear
tags:
- Amazon
- AWS
- Deployment
- DevOps
- CI/CD
- Release Management
- Blue/Green Deployment
title: TimeBasedLinear
---
