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
- list deployments for an application and deployment group
- manages deployment infrastructure.
- automated application deployment to compute targets.
- create a codedeploy application
- Release Manager
- create deployment group
- get details about a specific deployment
- create deployment
- managing software release processes and rollbacks.
- devops
- amazon
- get deployment
- create a deployment group for an application
- release management
- list deployments
- create a new deployment
- application deployment to ec2, lambda, ecs, and on-premises servers.
- list instances in a deployment
- get deployment information for a target instance
- DevOps Engineer
- create and monitor deployments
- list deployment groups
- deployment
- create application
- coordinates application releases.
- aws
- ci/cd
- list deployment instances
- list codedeploy applications
- get deployment instance
- list deployment groups for an application
- list applications
- manage codedeploy applications
- stop deployment
- blue/green deployment
- manage deployment groups
- stop an in-progress deployment
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
