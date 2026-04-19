---
api_count: 1
apis:
- description: The AWS Marketplace Catalog API provides programmatic access to manage entities and change sets for publishing and updating software products, data products, and machine learning products on AWS Marke
  name: AWS Marketplace Catalog API
  slug: aws-marketplace-catalog-api
capabilities:
- description: Workflow capability for ISV sellers and marketplace operators to publish, update, and manage software products and offers on AWS Marketplace using the Catalog API.
  name: Amazon Marketplace - Catalog Management Workflow
  slug: marketplace-catalog-workflow
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/marketplace/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/marketplace/
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
  url: https://aws.amazon.com/blogs/awsmarketplace/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/marketplace/
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
  url: rules/amazon-marketplace-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-marketplace-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/marketplace-catalog-workflow.yaml
created: '2026-03-16'
description: AWS Marketplace is a curated digital catalog that makes it easy to find, buy, deploy, and manage third-party software, data, and services that run on AWS. It offers thousands of software listings from independent software vendors. The Marketplace Catalog API enables programmatic management of marketplace entities including products, offers, and data products through change sets and entity description operations.
features:
- description: Programmatically list and describe marketplace entities including software products, data products, and offers.
  name: Entity Management
- description: Start, monitor, and cancel change sets for publishing new listings or updating existing ones.
  name: Change Set Lifecycle
- description: Attach, retrieve, and remove resource-based policies to control access to marketplace entities.
  name: Resource Policies
- description: Tag marketplace resources with key-value pairs for organization and cost allocation.
  name: Resource Tagging
- description: Access marketplace entities across multiple AWS regions through regional catalog endpoints.
  name: Multi-Region Support
- description: Integrate catalog API with CI/CD pipelines for automated product publishing and updates.
  name: Publishing Automation
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Control access to catalog API operations through IAM policies and roles.
  name: AWS IAM
- description: Subscribe to marketplace events for change set completions and entity state changes.
  name: Amazon EventBridge
- description: Deploy and manage marketplace subscriptions as infrastructure-as-code.
  name: AWS CloudFormation
- description: Share private marketplace listings across accounts in an AWS organization.
  name: AWS Organizations
- description: Receive notifications for marketplace change set status updates.
  name: Amazon SNS
jsonld:
- class_count: 33
  name: Amazon Marketplace Context
  property_count: 44
  slug: amazon-marketplace-context
layout: provider
modified: '2026-04-19'
name: Amazon Marketplace
rules:
- name: Amazon Marketplace API Rules
  rule_count: 18
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 7
  slug: amazon-marketplace-spectral-rules
skills: []
slug: amazon-marketplace
solutions: []
tags:
- AWS
- Commerce
- ISV
- Marketplace
- Software Catalog
url: https://raw.githubusercontent.com/api-evangelist/amazon-marketplace/refs/heads/main/apis.yml
use_cases:
- description: Automate publishing and updating software listings on AWS Marketplace from CI/CD pipelines.
  name: Product Publishing Automation
- description: Programmatically discover and evaluate available software products and data products.
  name: Marketplace Catalog Discovery
- description: Track the status of publishing operations and receive change set completion notifications.
  name: Change Set Monitoring
- description: Manage marketplace listings across multiple AWS accounts with shared resource policies.
  name: Multi-Account Marketplace Management
- description: Enable ISV teams to self-service publish and update product listings through the catalog API.
  name: ISV Self-Service Publishing
---
