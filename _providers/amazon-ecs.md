---
api_count: 4
apis:
- description: The Amazon ECS API provides programmatic access to manage containerized applications using Docker containers.
  name: Amazon ECS API
  slug: ''
- description: Amazon ECS Service Connect provides management of service-to-service communication as Amazon ECS configuration, building both service discovery and a service mesh for connecting services within and ac
  name: Amazon ECS Service Connect API
  slug: ''
- description: Amazon ECS Anywhere extends Amazon ECS to support registering external instances such as on-premises servers or virtual machines to your Amazon ECS cluster, allowing you to run and manage containerize
  name: Amazon ECS Anywhere API
  slug: ''
- description: AWS Copilot is an open source command line interface that simplifies building, releasing, and operating production-ready containerized applications on Amazon ECS and AWS Fargate, providing common clou
  name: AWS Copilot CLI
  slug: ''
capabilities:
- description: Container orchestration workflow for DevOps engineers and platform teams to manage ECS clusters, deploy services, run tasks, and monitor container workloads.
  name: Amazon ECS Container Orchestration
  slug: container-orchestration
common:
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/ecs/
- title: ''
  type: Pricing
  url: https://aws.amazon.com/ecs/pricing/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/ecs/faqs/
- title: ''
  type: GettingStarted
  url: https://aws.amazon.com/ecs/getting-started/
- title: ''
  type: Resources
  url: https://aws.amazon.com/ecs/resources/
- title: ''
  type: Partners
  url: https://aws.amazon.com/ecs/partners/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/aws/category/compute/amazon-elastic-container-service/
- title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- title: ''
  type: SDK
  url: https://aws.amazon.com/tools/
- title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/ecs/
- title: ''
  type: Security
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security.html
- title: ''
  type: Compliance
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-compliance.html
- title: ''
  type: BestPractices
  url: https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/intro.html
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-logging-monitoring.html
- title: ''
  type: Troubleshooting
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshooting.html
- title: ''
  type: Console
  url: https://console.aws.amazon.com/ecs/home
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/tags/TAd-wgX2x3QgSxyelEN6raFg/amazon-elastic-container-service
- title: ''
  type: ChangeLog
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/document_history.html
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-versions-changelog.html
- title: ''
  type: GitHubRepository
  url: https://github.com/aws/amazon-ecs-agent/releases
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
created: '2024'
description: Amazon Elastic Container Service (ECS) is a fully managed container orchestration service that makes it easy to deploy, manage, and scale containerized applications.
features:
- description: Run and manage Docker containers at scale without managing the underlying infrastructure or control plane.
  name: Fully Managed Container Orchestration
- description: Run containers serverlessly without provisioning or managing EC2 instances using AWS Fargate launch type.
  name: AWS Fargate Integration
- description: Automatically scale container workloads based on CloudWatch metrics, target tracking, or step scaling policies.
  name: Service Auto Scaling
- description: Built-in service discovery and service mesh for connecting containerized services within and across clusters.
  name: Service Connect
- description: Extend ECS to on-premises and edge infrastructure to run containers on your own servers and virtual machines.
  name: ECS Anywhere
- description: Manage compute capacity with capacity provider strategies for optimal resource allocation across EC2 and Fargate.
  name: Capacity Providers
- description: Define containerized applications as task definitions with CPU, memory, networking, and IAM role configurations.
  name: Task Definitions
- description: Monitor container performance metrics and logs with CloudWatch Container Insights for operational visibility.
  name: Container Insights
image: /assets/icons/amazon-ecs.png
integrations:
- description: Serverless compute engine for running containers without managing underlying EC2 instances.
  name: AWS Fargate
- description: Private container registry for storing, managing, and deploying Docker container images.
  name: Amazon ECR
- description: Infrastructure as code for provisioning and managing ECS clusters, services, and task definitions.
  name: AWS CloudFormation
- description: Distribute traffic across containers with Application Load Balancer and Network Load Balancer integration.
  name: Elastic Load Balancing
- description: Monitor container metrics, logs, and alarms with CloudWatch and Container Insights.
  name: Amazon CloudWatch
- description: Fine-grained access control for ECS tasks and services using IAM roles and policies.
  name: AWS IAM
jsonld:
- class_count: 0
  name: Amazon Ecs Context
  property_count: 0
  slug: amazon-ecs-context
layout: provider
modified: '2026-04-18'
name: Amazon ECS
rules:
- name: Amazon ECS API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: amazon-ecs-spectral-rules
skills: []
slug: amazon-ecs
solutions: []
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
url: https://aws.amazon.com/ecs/
use_cases:
- description: Deploy and manage microservices with independent scaling, deployment, and lifecycle management per service.
  name: Microservices Architecture
- description: Run batch computing workloads using ECS tasks with automatic scaling and job scheduling.
  name: Batch Processing
- description: Integrate with AWS CodePipeline and CodeDeploy for automated blue/green and rolling deployments of containerized applications.
  name: CI/CD Pipeline Deployment
- description: Run containerized workloads across AWS cloud and on-premises environments using ECS Anywhere.
  name: Hybrid Cloud Workloads
- description: Deploy ML models as containerized inference endpoints with auto-scaling based on demand.
  name: Machine Learning Inference
---
