---
api_count: 1
apis:
- description: Core API for managing Amazon Virtual Private Cloud resources including VPCs, subnets, internet gateways, NAT gateways, route tables, and network ACLs. VPC operations are part of the Amazon EC2 API.
  name: Amazon VPC API
  slug: ''
capabilities:
- description: ''
  name: Amazon Vpc Capability
  slug: amazon-vpc-capability
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/vpc/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/vpc/
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
  url: https://aws.amazon.com/blogs/networking-and-content-delivery/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/vpc/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Knowledge Center
  url: https://repost.aws/knowledge-center
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: Stack Overflow
  url: https://stackoverflow.com/questions/tagged/amazon-vpc
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Security
  url: https://docs.aws.amazon.com/vpc/latest/userguide/security.html
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc/refs/heads/main/rules/amazon-vpc-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc/refs/heads/main/vocabulary/amazon-vpc-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc/refs/heads/main/capabilities/amazon-vpc-capability.yaml
created: '2024-01-15'
description: Amazon Virtual Private Cloud (VPC) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define, with complete control over IP addressing, subnets, routing, and network gateways.
features:
- description: Automate operational tasks with Amazon VPC.
  name: Automation
- description: Programmatic access to Amazon VPC resources.
  name: API Access
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations: []
jsonld:
- class_count: 0
  name: Amazon Vpc Context
  property_count: 6
  slug: amazon-vpc-context
layout: provider
modified: '2026-04-19'
name: Amazon VPC
rules:
- name: Amazon VPC API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: amazon-vpc-spectral-rules
skills: []
slug: amazon-vpc
solutions: []
tags:
- AWS
- Networking
- Private Cloud
- Security
- Subnets
- VPC
url: https://aws.amazon.com/vpc/
use_cases:
- description: Use Amazon VPC to manage and automate cloud operations.
  name: Cloud Operations
---
