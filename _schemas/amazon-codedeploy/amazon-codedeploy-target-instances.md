---
description: Information about the instances to be used in the replacement environment in a blue/green deployment.
layout: schema
name: TargetInstances
properties_list:
- description: ''
  name: tagFilters
  type: object
- description: ''
  name: autoScalingGroups
  type: object
- description: ''
  name: ec2TagSet
  type: object
provider_name: Amazon CodeDeploy
provider_slug: amazon-codedeploy
schema_file: json-schema/amazon-codedeploy-target-instances-schema.json
slug: amazon-codedeploy-target-instances
tags:
- Amazon
- AWS
- Deployment
- DevOps
- CI/CD
- Release Management
- Blue/Green Deployment
title: TargetInstances
---
