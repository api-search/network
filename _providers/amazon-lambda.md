---
api_count: 1
apis:
- description: Core API for managing AWS Lambda functions, event source mappings, layers, aliases, versions, and permissions. Enables creating and invoking serverless functions, configuring triggers from AWS service
  name: Amazon Lambda API
  slug: ''
capabilities:
- description: Unified workflow capability for Amazon Lambda combining resource management and operations.
  name: Amazon Lambda Workflow
  slug: amazon-lambda-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Portal
  url: https://aws.amazon.com/lambda/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/lambda/
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
  url: https://aws.amazon.com/blogs/compute/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/lambda/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
- title: ''
  type: Status
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Knowledge Center
  url: https://repost.aws/knowledge-center
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: Stack Overflow
  url: https://stackoverflow.com/questions/tagged/aws-lambda
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Security
  url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-lambda-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-lambda-workflow.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-lambda-vocabulary.yaml
created: '2024-01-15'
description: AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers, automatically scaling and executing your code in response to events from over 200 AWS services and SaaS applications while you pay only for the compute time you consume.
features:
- description: Run code without provisioning or managing servers — Lambda handles all administration.
  name: Serverless Execution
- description: Automatically trigger code from over 200 AWS services and SaaS applications.
  name: Event-Driven Triggers
- description: Automatically scales to thousands of concurrent executions without configuration.
  name: Automatic Scaling
- description: Supports Node.js, Python, Java, Go, Ruby, .NET, and custom runtimes via Lambda layers.
  name: Multiple Runtimes
- description: Package and share code, libraries, and configurations across Lambda functions.
  name: Lambda Layers
- description: Deploy Lambda functions as container images up to 10 GB in size.
  name: Container Image Support
- description: Reduce cold starts for Java functions with Lambda SnapStart.
  name: SnapStart
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Build REST and WebSocket APIs backed by Lambda functions.
  name: Amazon API Gateway
- description: Trigger Lambda from DynamoDB Streams for real-time data processing.
  name: Amazon DynamoDB
- description: Trigger Lambda on S3 object events for serverless file processing.
  name: Amazon S3
- description: Process Kinesis data streams with Lambda for real-time analytics.
  name: Amazon Kinesis
- description: Orchestrate Lambda functions in serverless workflows.
  name: AWS Step Functions
- description: Process SQS messages with Lambda for decoupled event processing.
  name: Amazon SQS
jsonld:
- class_count: 2
  name: Amazon Lambda Context
  property_count: 7
  slug: amazon-lambda-context
layout: provider
modified: '2026-04-19'
name: Amazon Lambda
rules:
- name: Amazon Lambda API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 7
  slug: amazon-lambda-spectral-rules
skills: []
slug: amazon-lambda
solutions: []
tags:
- AWS
- Compute
- Event-Driven
- FaaS
- Functions
- Serverless
url: https://aws.amazon.com/lambda/
use_cases:
- description: Build REST and GraphQL API backends with Lambda and API Gateway.
  name: API Backends
- description: Process S3 uploads, DynamoDB streams, and Kinesis records in real time.
  name: Data Processing
- description: Automate operational tasks triggered by CloudWatch events or schedules.
  name: Event Automation
- description: Run ML model inference on-demand without managing inference infrastructure.
  name: Machine Learning Inference
---
