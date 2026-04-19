---
api_count: 1
apis:
- description: The AWS Fault Injection Simulator API provides programmatic access to create and manage experiment templates, experiments, and actions for conducting chaos engineering experiments on AWS workloads.
  name: AWS Fault Injection Simulator API
  slug: aws-fis-api
capabilities:
- description: Workflow capability for executing chaos engineering experiments using AWS FIS. Enables resilience engineers and SREs to design, execute, and monitor fault injection experiments across AWS infrastructu
  name: AWS FIS Chaos Engineering
  slug: amazon-fis-chaos-engineering
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/fis/
- title: ''
  type: Website
  url: https://aws.amazon.com/fis/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/fis/
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
  url: https://aws.amazon.com/blogs/devops/tag/aws-fault-injection-simulator/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/fis/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-fis
- title: ''
  type: SpectralRules
  url: rules/amazon-fis-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/fis.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-fis-chaos-engineering.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-fis-vocabulary.yaml
- title: ''
  type: JSON-LD
  url: json-ld/amazon-fis-context.jsonld
created: '2026-03-16'
description: AWS Fault Injection Simulator (FIS) is a fully managed service for running fault injection experiments on AWS. It allows you to improve an application's performance, observability, and resiliency by identifying and fixing weaknesses through controlled chaos engineering experiments.
features:
- description: Fully managed service requiring no agent installation with pre-built fault injection actions for EC2, RDS, ECS, EKS, and more.
  name: Managed Fault Injection
- description: Ready-to-use resilience scenarios for AZ failures, power interruptions, network disruptions, and cross-region connectivity issues.
  name: Pre-built Scenarios
- description: CloudWatch alarm-based stop conditions and safety levers prevent unintended impact during live testing.
  name: Safety Controls
- description: Tag-based resource targeting scopes experiments to specific environments, applications, or resource subsets.
  name: Fine-grained Targeting
- description: Run experiments across multiple AWS accounts using target account configurations.
  name: Multi-account Support
- description: API and CLI access enables automated resilience testing in deployment pipelines.
  name: CI/CD Integration
- description: Console and API provide real-time status of executing actions, affected resources, and triggered stop conditions.
  name: Real-time Visibility
- description: Fine-grained IAM controls restrict which users can create, run, or view experiments and affected resources.
  name: IAM Security
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Stop conditions use CloudWatch alarms to automatically halt experiments.
  name: Amazon CloudWatch
- description: Task execution roles define which AWS resources experiments can affect.
  name: AWS IAM
- description: Stop instances, terminate instances, and inject CPU/memory stress on EC2.
  name: Amazon EC2
- description: Stop ECS tasks and inject faults into containerized workloads.
  name: Amazon ECS
- description: Terminate Kubernetes nodes and pods running on EKS.
  name: Amazon EKS
- description: Trigger RDS failovers, reboot instances, and pause cluster I/O.
  name: Amazon RDS
- description: Inject latency and errors into Lambda function invocations.
  name: AWS Lambda
- description: Pause DynamoDB replication between replicas.
  name: Amazon DynamoDB
jsonld:
- class_count: 13
  name: Amazon Fis Context
  property_count: 23
  slug: amazon-fis-context
layout: provider
modified: '2026-04-19'
name: Amazon Fault Injection Simulator
rules:
- name: Amazon Fault Injection Simulator API Rules
  rule_count: 28
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 16
  slug: amazon-fis-spectral-rules
skills: []
slug: amazon-fault-injection-simulator
solutions: []
tags:
- AWS
- Chaos Engineering
- DevOps
- Fault Injection
- Resilience Testing
url: https://raw.githubusercontent.com/api-evangelist/amazon-fault-injection-simulator/refs/heads/main/apis.yml
use_cases:
- description: Validate application behavior under resource failures before they occur in production.
  name: Application Resilience Testing
- description: Run structured fault injection experiments following chaos engineering principles.
  name: Chaos Engineering
- description: Verify that monitoring and alerting systems detect and respond to failures correctly.
  name: Observability Validation
- description: Conduct planned game day exercises simulating failure scenarios for team readiness.
  name: Game Days
- description: Integrate resilience testing into CI/CD pipelines for continuous validation.
  name: Automated Pipeline Testing
- description: Test cross-region failover mechanisms and recovery time objectives.
  name: Multi-region Failover Testing
---
