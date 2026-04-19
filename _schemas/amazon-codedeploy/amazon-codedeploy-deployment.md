---
description: Represents an AWS CodeDeploy deployment with its configuration, status, and rollback settings.
layout: schema
name: Amazon CodeDeploy Deployment
properties_list:
- description: The unique ID of the deployment.
  name: deploymentId
  type: string
- description: The application name.
  name: applicationName
  type: string
- description: The deployment group name.
  name: deploymentGroupName
  type: string
- description: The current state of the deployment.
  name: status
  type: string
- description: The destination platform type for the deployment.
  name: computePlatform
  type: string
- description: Information about the location of stored application artifacts.
  name: revision
  type: object
- description: A comment about the deployment.
  name: description
  type: string
- description: The means by which the deployment was created.
  name: creator
  type: string
- description: A timestamp that indicates when the deployment was created.
  name: createTime
  type: string
- description: A timestamp that indicates when the deployment was deployed to the deployment group.
  name: startTime
  type: string
- description: A timestamp that indicates when the deployment was complete.
  name: completeTime
  type: string
- description: Information about the automatic rollback configuration.
  name: autoRollbackConfiguration
  type: object
- description: Information about a deployment rollback.
  name: rollbackInfo
  type: object
provider_name: Amazon CodeDeploy
provider_slug: amazon-codedeploy
schema_file: json-schema/amazon-codedeploy-deployment-schema.json
slug: amazon-codedeploy-deployment
tags:
- Amazon
- AWS
- Deployment
- DevOps
- CI/CD
- Release Management
- Blue/Green Deployment
title: Amazon CodeDeploy Deployment
---
