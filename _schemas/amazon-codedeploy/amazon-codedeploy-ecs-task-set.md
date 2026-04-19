---
description: Information about a set of Amazon ECS tasks in an CodeDeploy deployment. An Amazon ECS task set includes details such as the desired number of tasks, how many tasks are running, and whether the task set serves production traffic. An CodeDeploy application that uses the Amazon ECS compute platform deploys a containerized application in an Amazon ECS service as a task set.
layout: schema
name: ECSTaskSet
properties_list:
- description: ''
  name: identifer
  type: object
- description: ''
  name: desiredCount
  type: object
- description: ''
  name: pendingCount
  type: object
- description: ''
  name: runningCount
  type: object
- description: ''
  name: status
  type: object
- description: ''
  name: trafficWeight
  type: object
- description: ''
  name: targetGroup
  type: object
- description: ''
  name: taskSetLabel
  type: object
provider_name: Amazon CodeDeploy
provider_slug: amazon-codedeploy
schema_file: json-schema/amazon-codedeploy-ecs-task-set-schema.json
slug: amazon-codedeploy-ecs-task-set
tags:
- Amazon
- AWS
- Deployment
- DevOps
- CI/CD
- Release Management
- Blue/Green Deployment
title: ECSTaskSet
---
