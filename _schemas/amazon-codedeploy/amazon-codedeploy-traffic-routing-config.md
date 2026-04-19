---
description: The configuration that specifies how traffic is shifted from one version of a Lambda function to another version during an Lambda deployment, or from one Amazon ECS task set to another during an Amazon ECS deployment.
layout: schema
name: TrafficRoutingConfig
properties_list:
- description: ''
  name: type
  type: object
- description: ''
  name: timeBasedCanary
  type: object
- description: ''
  name: timeBasedLinear
  type: object
provider_name: Amazon CodeDeploy
provider_slug: amazon-codedeploy
schema_file: json-schema/amazon-codedeploy-traffic-routing-config-schema.json
slug: amazon-codedeploy-traffic-routing-config
tags:
- Amazon
- AWS
- Deployment
- DevOps
- CI/CD
- Release Management
- Blue/Green Deployment
title: TrafficRoutingConfig
---
