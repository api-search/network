---
api_count: 1
apis:
- description: Core API for creating and managing state machines and executions in AWS Step Functions, enabling serverless workflow orchestration for coordinating distributed applications and microservices.
  name: Amazon Step Functions API
  slug: ''
capabilities: []
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/step-functions/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/step-functions/latest/apireference/Welcome.html
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
  url: https://aws.amazon.com/blogs/compute/category/application-services/aws-step-functions/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/states/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-step-functions-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-step-functions-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/amazon-step-functions.yaml
created: '2024-01-15'
description: Amazon Step Functions is a serverless workflow orchestration service that lets you coordinate distributed applications and microservices using visual workflows, enabling you to build and update state machines that react to events, manage retries, and orchestrate complex business processes.
features:
- description: Design and visualize workflows using Amazon States Language (ASL).
  name: Visual Workflow
- description: Orchestrate Lambda, ECS, Fargate, SNS, SQS, and 220+ AWS services.
  name: Serverless Orchestration
- description: Built-in retry and catch capabilities for fault-tolerant workflows.
  name: Error Handling
- description: High-throughput workflows for event processing at scale.
  name: Express Workflows
- description: Long-running durable workflows with exactly-once execution.
  name: Standard Workflows
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Invoke Lambda functions as workflow steps.
  name: AWS Lambda
- description: Run ECS/Fargate tasks as part of workflows.
  name: Amazon ECS
- description: Read and write DynamoDB tables directly from workflows.
  name: Amazon DynamoDB
- description: Publish SNS notifications from workflow steps.
  name: Amazon SNS
- description: Orchestrate ML training and inference pipelines.
  name: Amazon SageMaker
- description: Run Glue ETL jobs from workflow steps.
  name: AWS Glue
jsonld:
- class_count: 121
  name: Amazon Step Functions Context
  property_count: 118
  slug: amazon-step-functions-context
layout: provider
modified: '2026-04-19'
name: Amazon Step Functions
rules:
- name: Amazon Step Functions API Rules
  rule_count: 19
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 7
  slug: amazon-step-functions-spectral-rules
skills: []
slug: amazon-step-functions
solutions: []
tags:
- AWS
- Orchestration
- Serverless
- State Machine
- Workflow
url: https://aws.amazon.com/step-functions/
use_cases:
- description: Coordinate multiple microservices into cohesive workflows.
  name: Microservice Orchestration
- description: Build ETL and data transformation pipelines with automatic retries.
  name: Data Processing Pipelines
- description: Automate IT and business processes with visual workflow design.
  name: IT Automation
- description: Orchestrate SageMaker model training, evaluation, and deployment.
  name: ML Model Training Pipelines
---
