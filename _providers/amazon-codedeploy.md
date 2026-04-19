---
api_count: 1
apis:
- description: 'The Amazon CodeDeploy REST API enables programmatic management of applications, deployment groups, deployment configurations, and deployments. Create and update deployment groups, trigger deployments '
  name: Amazon CodeDeploy API
  slug: amazon-codedeploy-api
capabilities:
- description: Unified workflow for DevOps teams to create deployment groups, deploy revisions to EC2, Lambda, and ECS targets, and monitor deployment status.
  name: Amazon CodeDeploy Deployment Automation
  slug: amazon-codedeploy-deployment-automation
common:
- title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-codedeploy.html
- title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/codedeploy/latest/userguide/auth-and-access-control.html
- title: ''
  type: Pricing
  url: https://aws.amazon.com/codedeploy/pricing/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/codedeploy/
- title: ''
  type: Portal
  url: https://aws.amazon.com/codedeploy/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/codedeploy/latest/userguide/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/devops/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/codedeploy/faqs/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/gp/aws/developer/registration/index.html
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: SpectralRules
  url: rules/amazon-codedeploy-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-codedeploy-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-codedeploy-deployment-automation.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-codedeploy-context.jsonld
created: '2026-03-16'
description: AWS CodeDeploy is a fully managed deployment service that automates software deployments to various compute services such as Amazon EC2, AWS Fargate, AWS Lambda, and on-premises servers. CodeDeploy makes it easier to rapidly release new features, helps avoid downtime during application deployment, and handles the complexity of updating your applications with in-place, blue/green, and canary deployment strategies.
features:
- description: Support for in-place, blue/green, and canary deployment strategies across EC2, Lambda, ECS, and on-premises targets to minimize downtime and risk.
  name: Multiple Deployment Strategies
- description: Automatically roll back deployments if a specified number of instances fail health checks or if CloudWatch alarms are triggered during deployment.
  name: Automated Rollbacks
- description: Define custom lifecycle event hooks (BeforeInstall, AfterInstall, ApplicationStart, etc.) using scripts or Lambda functions for fine-grained deployment control.
  name: Deployment Lifecycle Hooks
- description: Implement canary and linear traffic shifting for Lambda function updates and ECS service deployments with configurable traffic weights and bake times.
  name: Traffic Shifting for Lambda and ECS
- description: Organize deployment targets using deployment groups with EC2 instance tags, Auto Scaling groups, ECS clusters, or on-premises instance tags.
  name: Deployment Groups
- description: Install the CodeDeploy agent on EC2 or on-premises instances to enable deployment target registration and lifecycle hook execution.
  name: CodeDeploy Agent
- description: Integrate with Application Load Balancers and Network Load Balancers for blue/green deployments that shift traffic between original and replacement instances.
  name: Integration with AWS Load Balancers
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Use CodeDeploy as the deployment stage in CodePipeline CD pipelines.
  name: AWS CodePipeline
- description: Trigger CodeDeploy deployments from build artifacts produced by CodeBuild.
  name: AWS CodeBuild
- description: Deploy Lambda function updates with traffic shifting strategies.
  name: AWS Lambda
- description: Deploy ECS service updates with blue/green deployments.
  name: Amazon ECS
- description: Trigger automatic rollbacks based on CloudWatch alarm states.
  name: AWS CloudWatch
- description: Integrate with ALB and NLB for blue/green traffic shifting.
  name: Elastic Load Balancing
- description: Deploy to Auto Scaling groups with automatic instance health checking.
  name: Amazon EC2 Auto Scaling
- description: Use SSM Run Command and State Manager for deployment automation.
  name: AWS Systems Manager
- description: Deploy application revisions stored in GitHub repositories.
  name: GitHub
- description: Store and retrieve application deployment bundles from S3.
  name: Amazon S3
jsonld:
- class_count: 16
  name: Amazon Codedeploy Context
  property_count: 29
  slug: amazon-codedeploy-context
layout: provider
modified: '2026-04-19'
name: Amazon CodeDeploy
rules:
- name: Amazon CodeDeploy API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 3
  slug: amazon-codedeploy-spectral-rules
skills: []
slug: amazon-codedeploy
solutions: []
tags:
- Amazon
- AWS
- Deployment
- DevOps
- CI/CD
- Release Management
- Blue/Green Deployment
url: https://raw.githubusercontent.com/api-evangelist/amazon-codedeploy/refs/heads/main/apis.yml
use_cases:
- description: Use blue/green deployments to update applications without downtime by routing traffic to a new environment while keeping the original environment available for rollback.
  name: Zero-Downtime Application Updates
- description: Deploy new Lambda function versions with canary or linear traffic shifting to gradually migrate traffic from the current version to the updated function version.
  name: Lambda Function Updates
- description: Deploy updated container tasks to ECS services with blue/green deployments and configurable traffic shifting through an Application Load Balancer.
  name: ECS Service Deployment
- description: Extend cloud-based deployment automation to on-premises servers using the CodeDeploy agent and on-premises instance registration.
  name: On-Premises Application Deployment
- description: Use CodeDeploy as the deployment stage in an AWS CodePipeline for fully automated continuous delivery from source code to production.
  name: Multi-Stage CD Pipeline
---
