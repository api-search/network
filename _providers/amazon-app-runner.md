---
api_count: 1
apis:
- description: 'The AWS App Runner API enables programmatic management of App Runner services, including creating and managing services, auto scaling configurations, custom domains, VPC connectors, and observability '
  name: Amazon App Runner API
  slug: ''
capabilities:
- description: Workflow for managing Amazon App Runner API resources.
  name: App Runner Management
  slug: app-runner-management
common:
- title: ''
  type: Portal
  url: https://console.aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/apprunner/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/apprunner/
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
  url: https://aws.amazon.com/blogs/containers/category/compute/aws-app-runner/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/apprunner
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: Service Status
  url: https://status.aws.amazon.com/
- title: ''
  type: Knowledge Center
  url: https://repost.aws/knowledge-center
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-app-runner
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Security
  url: https://aws.amazon.com/security/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-app-runner-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/app-runner-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-app-runner-vocabulary.yaml
created: '2024-01-15'
description: AWS App Runner is a fully managed container application service that lets you build, deploy, and run containerized web applications and API services without prior infrastructure or container experience. Start with your source code or a container image.
features:
- description: Create, update, and delete App Runner services that deploy containerized or source-code-based web applications without managing infrastructure.
  name: Service Management
- description: Configure auto scaling policies to automatically scale App Runner services in and out based on traffic demand.
  name: Auto Scaling Configuration
- description: Associate custom domains with App Runner services for branded URLs with automatic SSL certificate provisioning.
  name: Custom Domain Support
- description: Connect App Runner services to VPC resources using VPC connectors for secure access to databases and internal services.
  name: VPC Connector Integration
- description: Configure automatic deployments triggered by source code changes or image push events for continuous delivery.
  name: Deployment Automation
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Deploy App Runner services directly from container images stored in Amazon ECR with automatic image updates.
  name: AWS ECR
- description: Use CodeBuild for source code building and integrate with App Runner for automated deployment pipelines.
  name: AWS CodeBuild
- description: Connect App Runner services to RDS databases using VPC connectors for secure private network access.
  name: Amazon RDS
- description: Monitor App Runner service metrics, request counts, and latency using CloudWatch dashboards and alarms.
  name: AWS CloudWatch
jsonld:
- class_count: 0
  name: Amazon App Runner Context
  property_count: 4
  slug: amazon-app-runner-context
layout: provider
modified: '2026-04-19'
name: Amazon App Runner
rules:
- name: Amazon App Runner API Rules
  rule_count: 3
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 0
  slug: amazon-app-runner-spectral-rules
skills: []
slug: amazon-app-runner
solutions: []
tags:
- AWS
- CI/CD
- Containers
- Deployment
- Managed Service
- Serverless
- Web Applications
url: https://raw.githubusercontent.com/api-evangelist/amazon-app-runner/refs/heads/main/apis.yml
use_cases:
- description: Deploy REST APIs and microservices as containers on App Runner with automatic scaling and zero infrastructure management.
  name: Containerized API Deployment
- description: Host web applications built from source code or container images with built-in load balancing and HTTPS.
  name: Web Application Hosting
- description: Integrate App Runner with CI/CD pipelines for automated service deployments triggered by repository changes.
  name: CI/CD Integration
- description: Quickly launch and scale web backends without DevOps expertise using App Runner managed infrastructure.
  name: Startup Companies
---
