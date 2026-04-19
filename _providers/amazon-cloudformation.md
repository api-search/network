---
api_count: 1
apis:
- description: API for creating, updating, and managing CloudFormation stacks, stack sets, and change sets for infrastructure-as-code deployments across AWS accounts and regions.
  name: Amazon CloudFormation API
  slug: ''
capabilities:
- description: Workflow for infrastructure as code deployment using Amazon CloudFormation for DevOps Engineer personas.
  name: Amazon CloudFormation Infrastructure as Code Deployment
  slug: infrastructure-as-code
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/cloudformation/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/
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
  url: https://aws.amazon.com/blogs/devops/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudformation/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-cloudformation
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-cloudformation-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloudformation-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/infrastructure-as-code.yaml
created: '2024-01-01'
description: AWS CloudFormation is an infrastructure-as-code service that speeds up cloud provisioning by enabling developers to define and manage AWS resources programmatically through templates. Scale infrastructure globally and manage resources across all AWS accounts and regions through a single operation.
features:
- description: Define AWS resources in JSON or YAML templates for repeatable, version-controlled deployments.
  name: Infrastructure as Code
- description: Deploy stacks across multiple AWS accounts and regions with a single operation.
  name: Multi-Account Stack Sets
- description: Preview changes to running stacks before executing them to avoid unintended updates.
  name: Change Sets
- description: Detect when deployed infrastructure has drifted from the CloudFormation template definition.
  name: Drift Detection
- description: Extend CloudFormation to manage third-party and community resources through the Registry.
  name: Registry Extensions
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Automate CloudFormation deployments in CI/CD pipelines.
  name: AWS CodePipeline
- description: Track infrastructure changes and detect drift with Config integration.
  name: AWS Config
- description: Control who can create and update CloudFormation stacks.
  name: AWS IAM
- description: Publish approved CloudFormation templates as self-service products.
  name: AWS Service Catalog
- description: Receive stack event notifications via SNS topics.
  name: Amazon SNS
jsonld:
- class_count: 16
  name: Amazon Cloudformation Context
  property_count: 50
  slug: amazon-cloudformation-context
layout: provider
modified: '2026-04-19'
name: Amazon CloudFormation
rules:
- name: Amazon CloudFormation API Rules
  rule_count: 19
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 6
  slug: amazon-cloudformation-spectral-rules
skills: []
slug: amazon-cloudformation
solutions: []
tags:
- AWS
- CloudFormation
- Infrastructure as Code
- DevOps
- IaC
url: https://raw.githubusercontent.com/api-evangelist/amazon-cloudformation/refs/heads/main/apis.yml
use_cases:
- description: Automate infrastructure testing and deployment through CI/CD pipelines.
  name: DevOps Automation
- description: Deploy consistent infrastructure across multiple AWS regions.
  name: Multi-Region Deployment
- description: Enforce organizational infrastructure standards through template guardrails.
  name: Compliance Governance
- description: Rapidly rebuild infrastructure from templates after failures.
  name: Disaster Recovery
---
