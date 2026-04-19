---
consumed_apis:
- codedeploy
description: Unified workflow for DevOps teams to create deployment groups, deploy revisions to EC2, Lambda, and ECS targets, and monitor deployment status.
layout: capability
name: Amazon CodeDeploy Deployment Automation
operations: []
personas: []
provider_name: Amazon CodeDeploy
provider_slug: amazon-codedeploy
search_terms:
- devops
- automated application deployment to compute targets.
- manage codedeploy applications
- list deployment groups
- list deployment groups for an application
- create deployment
- get details about a specific deployment
- manage deployment groups
- list instances in a deployment
- create deployment group
- list codedeploy applications
- stop deployment
- list deployment instances
- application deployment to ec2, lambda, ecs, and on-premises servers.
- manages deployment infrastructure.
- list deployments for an application and deployment group
- DevOps Engineer
- get deployment
- create and monitor deployments
- aws
- get deployment instance
- create a codedeploy application
- Release Manager
- amazon
- managing software release processes and rollbacks.
- list applications
- get deployment information for a target instance
- list deployments
- ci/cd
- create a deployment group for an application
- release management
- create a new deployment
- deployment
- coordinates application releases.
- stop an in-progress deployment
- blue/green deployment
- create application
slug: amazon-codedeploy-deployment-automation
tags:
- Amazon
- AWS
- Deployment
- DevOps
- CI/CD
- Release Management
tools:
- description: List CodeDeploy applications
  hints:
    openWorld: true
    readOnly: true
  name: list-applications
- description: Create a CodeDeploy application
  hints:
    openWorld: false
    readOnly: false
  name: create-application
- description: List deployment groups for an application
  hints:
    openWorld: true
    readOnly: true
  name: list-deployment-groups
- description: Create a new deployment
  hints:
    openWorld: false
    readOnly: false
  name: create-deployment
- description: Get details about a specific deployment
  hints:
    openWorld: true
    readOnly: true
  name: get-deployment
- description: List deployments for an application and deployment group
  hints:
    openWorld: true
    readOnly: true
  name: list-deployments
- description: Stop an in-progress deployment
  hints:
    destructive: false
    openWorld: false
    readOnly: false
  name: stop-deployment
- description: Get deployment information for a target instance
  hints:
    openWorld: true
    readOnly: true
  name: get-deployment-instance
- description: List instances in a deployment
  hints:
    openWorld: true
    readOnly: true
  name: list-deployment-instances
- description: Create a deployment group for an application
  hints:
    openWorld: false
    readOnly: false
  name: create-deployment-group
---
