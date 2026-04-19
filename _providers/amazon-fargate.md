---
api_count: 1
apis:
- description: The Amazon Fargate API is accessed through Amazon ECS and enables you to run containers without managing servers or clusters. You can define tasks, configure networking and IAM policies, and deploy co
  name: Amazon Fargate API
  slug: ''
capabilities:
- description: Workflow capability for deploying and managing serverless container workloads on Amazon Fargate. Combines cluster management, task definitions, task execution, and service deployment for platform engi
  name: Amazon Fargate Container Orchestration
  slug: amazon-fargate-container-orchestration
common:
- title: ''
  type: Portal
  url: https://console.aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/fargate/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/containers/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/ecs
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-fargate
- title: ''
  type: SpectralRules
  url: rules/amazon-fargate-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/fargate.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-fargate-container-orchestration.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-fargate-vocabulary.yaml
- title: ''
  type: JSON-LD
  url: json-ld/amazon-fargate-context.jsonld
created: '2024-01-15'
description: Amazon Fargate is a serverless compute engine for containers that works with both Amazon ECS and Amazon EKS. Fargate removes the need to provision and manage servers, letting you specify and pay for resources per application, and improves security through application isolation by design.
features:
- description: Run containers without provisioning or managing servers. Fargate handles capacity, OS updates, and scaling automatically.
  name: Serverless Compute
- description: Works seamlessly with both Amazon ECS task definitions and Amazon EKS pods.
  name: ECS and EKS Integration
- description: Each task runs in its own dedicated single-tenant compute environment for improved security.
  name: Workload Isolation
- description: Tasks receive ENIs with full VPC networking support including security groups and VPC Flow Logs.
  name: VPC Networking
- description: Supports Application Auto Scaling with target tracking, step scaling, and scheduled scaling.
  name: Auto Scaling
- description: Integration with Amazon EFS for stateful workloads requiring persistent storage.
  name: Persistent Storage
- description: HIPAA, PCI, FedRAMP, and GovCloud (US) region support for regulated workloads.
  name: Compliance Support
- description: Built-in Container Insights for metrics, logs, and observability.
  name: CloudWatch Integration
- description: Run workloads on AWS Graviton processors for improved price-performance.
  name: ARM64/Graviton Support
- description: Run fault-tolerant workloads on Fargate Spot for significant cost savings.
  name: Spot Instances
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Primary orchestration engine for running Fargate tasks and services.
  name: Amazon ECS
- description: Run Kubernetes pods serverlessly using Fargate profiles.
  name: Amazon EKS
- description: Fine-grained task-level IAM roles for container security and least privilege.
  name: AWS IAM
- description: Container Insights, metrics, logs, and alarms for Fargate workloads.
  name: Amazon CloudWatch
- description: Automatically scale Fargate services based on CloudWatch metrics.
  name: AWS Application Auto Scaling
- description: Persistent shared file storage for stateful Fargate workloads.
  name: Amazon EFS
- description: Run high-scale batch workloads using Fargate compute environments.
  name: AWS Batch
- description: Route HTTP/HTTPS traffic to Fargate services using ALB target groups.
  name: Application Load Balancer
- description: Inject secrets and configuration into Fargate task containers securely.
  name: AWS Secrets Manager
- description: Store and deploy container images from Amazon Elastic Container Registry.
  name: Amazon ECR
jsonld:
- class_count: 18
  name: Amazon Fargate Context
  property_count: 61
  slug: amazon-fargate-context
layout: provider
modified: '2026-04-19'
name: Amazon Fargate
rules:
- name: Amazon Fargate API Rules
  rule_count: 29
  severity_counts:
    error: 10
    hint: 0
    info: 4
    warn: 15
  slug: amazon-fargate-spectral-rules
skills: []
slug: amazon-fargate
solutions: []
tags:
- AWS
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
url: https://aws.amazon.com/fargate/
use_cases:
- description: Deploy microservices-based web applications and REST APIs without infrastructure management.
  name: Web Applications and APIs
- description: Run parallel data processing jobs and ETL workloads using AWS Batch with Fargate.
  name: Batch Data Processing
- description: Lift-and-shift containerized workloads to serverless infrastructure for reduced operational burden.
  name: Application Modernization
- description: Run training, inference, and data preparation containers in flexible serverless environments.
  name: AI/ML Workloads
- description: Execute build, test, and deployment pipelines as ephemeral Fargate tasks.
  name: CI/CD Pipelines
- description: Run time-based container workloads using Amazon EventBridge and Fargate tasks.
  name: Scheduled Jobs
---
