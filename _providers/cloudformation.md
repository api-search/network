---
api_count: 2
apis:
- description: AWS CloudFormation gives you an easy way to model a collection of related AWS and third-party resources, provision them quickly and consistently, and manage them throughout their lifecycles. It uses t
  name: AWS CloudFormation API
  slug: ''
- description: 'AWS Cloud Control API provides a uniform CRUDL (create, read, update, delete, list) interface for managing AWS and third-party resources. It offers a standardized way to access and provision resource '
  name: AWS Cloud Control API
  slug: ''
capabilities:
- description: Unified workflow for AWS infrastructure provisioning combining CloudFormation stack management with Cloud Control API resource operations. Used by cloud engineers and platform teams to define, deploy,
  name: AWS Infrastructure Provisioning
  slug: infrastructure-provisioning
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/cloudformation/resources/
- title: ''
  type: GettingStarted
  url: https://aws.amazon.com/cloudformation/getting-started/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/
- title: ''
  type: Pricing
  url: https://aws.amazon.com/cloudformation/pricing/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/devops/category/management-tools/aws-cloudformation/
- title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudformation/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws-cloudformation
- title: ''
  type: GitHubRepository
  url: https://github.com/aws-cloudformation/aws-cloudformation-templates
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-cloudformation
- title: Python SDK (Boto3)
  type: SDK
  url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html
- title: JavaScript SDK v3
  type: SDK
  url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/cloudformation-examples.html
- title: Java SDK
  type: SDK
  url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-cloudformation.html
- title: Go SDK
  type: SDK
  url: https://docs.aws.amazon.com/sdk-for-go/api/service/cloudformation/
- title: AWS CLI - CloudFormation
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/cloudformation/
- title: Rain - CloudFormation CLI
  type: CLI
  url: https://github.com/aws-cloudformation/rain
- title: Stack Schema
  type: JSONSchema
  url: json-schema/stack.json
- title: Template Schema
  type: JSONSchema
  url: json-schema/template.json
- title: Resource Schema
  type: JSONSchema
  url: json-schema/resource.json
- title: Change Set Schema
  type: JSONSchema
  url: json-schema/change-set.json
- title: Change Schema
  type: JSONSchema
  url: json-schema/cloudformation-change-schema.json
- title: Change Set Detail Schema
  type: JSONSchema
  url: json-schema/cloudformation-change-set-detail-schema.json
- title: Change Set Summary Schema
  type: JSONSchema
  url: json-schema/cloudformation-change-set-summary-schema.json
- title: Error Response Schema
  type: JSONSchema
  url: json-schema/cloudformation-error-response-schema.json
- title: Stack Detail Schema
  type: JSONSchema
  url: json-schema/cloudformation-stack-schema.json
- title: Stack Event Schema
  type: JSONSchema
  url: json-schema/cloudformation-stack-event-schema.json
- title: Stack Resource Schema
  type: JSONSchema
  url: json-schema/cloudformation-stack-resource-schema.json
- title: Stack Summary Schema
  type: JSONSchema
  url: json-schema/cloudformation-stack-summary-schema.json
- title: Tag Schema
  type: JSONSchema
  url: json-schema/cloudformation-tag-schema.json
- title: Cloud Control Progress Event Schema
  type: JSONSchema
  url: json-schema/cloud-control-progress-event-schema.json
- title: Cloud Control Resource Description Schema
  type: JSONSchema
  url: json-schema/cloud-control-resource-description-schema.json
- title: Cloud Control Error Response Schema
  type: JSONSchema
  url: json-schema/cloud-control-error-response-schema.json
- title: JSON-LD Context
  type: JSONLD
  url: json-ld/context.jsonld
- title: CloudFormation JSON-LD Context
  type: JSONLD
  url: json-ld/cloudformation-context.jsonld
- title: Cloud Control JSON-LD Context
  type: JSONLD
  url: json-ld/cloud-control-context.jsonld
- title: CloudFormation Vocabulary
  type: Vocabulary
  url: vocabulary/cloudformation-vocabulary.yaml
- title: Spectral Rules
  type: Rules
  url: rules/cloudformation-spectral-rules.yml
- title: Infrastructure Provisioning Workflow
  type: Capabilities
  url: capabilities/infrastructure-provisioning.yaml
- title: CloudFormation Shared Capability
  type: Capabilities
  url: capabilities/shared/cloudformation.yaml
- title: Cloud Control Shared Capability
  type: Capabilities
  url: capabilities/shared/cloud-control.yaml
created: '2024'
description: A collection of APIs provided by AWS for infrastructure as code provisioning and management of AWS and third-party resources using CloudFormation templates and the Cloud Control API.
features:
- description: Define and provision AWS infrastructure using declarative JSON/YAML templates
  name: Infrastructure As Code
- description: Create, update, and delete collections of AWS resources as a single unit
  name: Stack Management
- description: Preview changes before applying them to running stacks
  name: Change Sets
- description: Detect when stack resources have been modified outside of CloudFormation
  name: Drift Detection
- description: Deploy stacks across multiple accounts and regions simultaneously
  name: Stack Sets
- description: Uniform interface for managing any resource in the CloudFormation Registry
  name: Cloud Control CRUDL
image: https://aws.amazon.com/cloudformation/logo.png
integrations:
- description: Define cloud infrastructure using familiar programming languages that compile to CloudFormation
  name: AWS CDK
- description: Simplified syntax for serverless application deployment via CloudFormation
  name: AWS SAM
- description: Alternative IaC tool that can import/export CloudFormation templates
  name: Terraform
jsonld:
- class_count: 0
  name: Cloud Control Context
  property_count: 0
  slug: cloud-control-context
- class_count: 0
  name: Cloudformation Context
  property_count: 0
  slug: cloudformation-context
- class_count: 0
  name: context Context
  property_count: 8
  slug: context
layout: provider
modified: '2026-04-18'
name: AWS CloudFormation
rules:
- name: AWS CloudFormation API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: cloudformation-spectral-rules
skills: []
slug: cloudformation
solutions: []
tags:
- Automation
- AWS
- Cloud Resources
- IaC
- Infrastructure As Code
- Stack Management
url: https://docs.aws.amazon.com/cloudformation/
use_cases:
- description: Deploy consistent infrastructure across multiple AWS accounts with Stack Sets
  name: Multi-Account Deployment
- description: Spin up identical dev, staging, and production environments from templates
  name: Environment Provisioning
- description: Detect configuration drift and enforce infrastructure compliance
  name: Compliance Auditing
---
