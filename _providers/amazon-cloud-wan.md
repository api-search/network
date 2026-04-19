---
api_count: 1
apis:
- description: API for building and managing global wide area networks, connecting branch offices, data centers, and VPCs with centralized control, monitoring, and network policy automation.
  name: Amazon Cloud WAN API
  slug: ''
capabilities:
- description: Workflow for wan management using Amazon Cloud WAN for Network Engineer personas.
  name: Amazon Cloud WAN WAN Management
  slug: wan-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/cloud-wan/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/
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
  url: https://console.aws.amazon.com/networkmanager/
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
  url: https://stackoverflow.com/questions/tagged/aws-cloud-wan
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-cloud-wan-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloud-wan-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/wan-management.yaml
created: '2026-03-16'
description: Amazon Cloud WAN is a managed wide area networking service that simplifies building, managing, and monitoring global WANs by connecting branch offices, data centers, and Amazon VPCs through a central dashboard with network policy automation and unified monitoring.
features:
- description: Build and manage global wide area networks through a single centralized dashboard.
  name: Centralized WAN Management
- description: Automate management and security tasks across your entire WAN infrastructure.
  name: Network Policy Automation
- description: Monitor on-premises and AWS network health and performance from one view.
  name: Unified Monitoring
- description: Isolate sensitive traffic from standard data flows with segmentation policies.
  name: Network Segmentation
- description: Connect branch offices, data centers, and VPCs with minimal configuration globally.
  name: Global Connectivity
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Connect VPCs and on-premises networks through Transit Gateway attachments.
  name: AWS Transit Gateway
- description: Dedicated network connections from on-premises to AWS.
  name: AWS Direct Connect
- description: Connect VPCs across regions into the global WAN.
  name: Amazon VPC
- description: Control access to Cloud WAN resources with IAM policies.
  name: AWS IAM
jsonld:
- class_count: 7
  name: Amazon Cloud Wan Context
  property_count: 9
  slug: amazon-cloud-wan-context
layout: provider
modified: '2026-04-19'
name: Amazon Cloud WAN
rules:
- name: Amazon Cloud WAN API Rules
  rule_count: 19
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 6
  slug: amazon-cloud-wan-spectral-rules
skills: []
slug: amazon-cloud-wan
solutions: []
tags:
- AWS
- Cloud WAN
- Networking
- Wide Area Network
- SD-WAN
url: https://raw.githubusercontent.com/api-evangelist/amazon-cloud-wan/refs/heads/main/apis.yml
use_cases:
- description: Build globally distributed corporate WANs using AWS infrastructure.
  name: Global Enterprise WAN
- description: Extend on-premises corporate WANs into AWS cloud environments seamlessly.
  name: Hybrid Network Extension
- description: Centralize network configuration, monitoring, and automation across all locations.
  name: Network Centralization
---
