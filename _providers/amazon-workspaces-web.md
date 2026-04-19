---
api_count: 1
apis:
- description: 'The Amazon WorkSpaces Web API provides programmatic access to create and manage web portals, network settings, user access logging, user settings, browser settings, and trust store configurations for '
  name: Amazon WorkSpaces Web API
  slug: amazon-workspaces-web-api
capabilities:
- description: Unified workflow for IT administrators to manage Amazon WorkSpaces Web portals, user settings, browser policies, network configurations, and trust stores for enterprise secure browser deployments.
  name: Amazon WorkSpaces Web Secure Browser Management
  slug: secure-browser-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/workspaces/web/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/workspaces-web/
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
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: SpectralRules
  url: rules/amazon-workspaces-web-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-workspaces-web-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/secure-browser-management.yaml
created: '2026-03-16'
description: Amazon WorkSpaces Web is a purpose-built, low-cost, fully managed service that enables secure browser access to internal websites and SaaS applications. It provides persistent browser sessions with built-in security controls, preventing users from downloading content to local devices while maintaining a seamless browsing experience. The service offers 58 API operations for managing portals, user settings, browser policies, network settings, trust stores, and IP access controls.
features:
- description: Purpose-built browser portals that provide secure access to internal websites and SaaS applications without VPN requirements.
  name: Secure Browser Portals
- description: Built-in controls to prevent users from downloading, uploading, printing, or copying content to local devices.
  name: Data Loss Prevention Controls
- description: Configurable browser policies to control features like clipboard access, printing, and file transfers at the organizational level.
  name: Browser Policy Management
- description: VPC-based network settings to isolate browser sessions within enterprise network boundaries with security group controls.
  name: Network Isolation
- description: SSL certificate trust stores for validating internal website certificates in secure browser sessions.
  name: Trust Store Management
- description: IP-based access rules to restrict portal access to specific corporate IP ranges or geographic locations.
  name: IP Access Controls
- description: Detailed session logging for audit and compliance purposes with integration to Kinesis data streams.
  name: User Access Logging
- description: SAML-based identity provider integration for single sign-on to secure browser portal sessions.
  name: Identity Integration
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Single sign-on integration for WorkSpaces Web portal authentication.
  name: AWS IAM Identity Center
- description: User access logging integration to stream session data for analysis.
  name: Amazon Kinesis
- description: Encryption key management for browser settings and data at rest.
  name: AWS KMS
- description: VPC integration for network isolation of browser sessions.
  name: Amazon VPC
- description: Certificate management for trust store and SSL configurations.
  name: AWS Certificate Manager
jsonld:
- class_count: 139
  name: Amazon Workspaces Web Context
  property_count: 63
  slug: amazon-workspaces-web-context
layout: provider
modified: '2026-04-19'
name: Amazon WorkSpaces Web
rules:
- name: Amazon WorkSpaces Web API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 7
  slug: amazon-workspaces-web-spectral-rules
skills: []
slug: amazon-workspaces-web
solutions: []
tags:
- AWS
- End User Computing
- Secure Browser
- Virtual Desktop
- Zero Trust
url: https://raw.githubusercontent.com/api-evangelist/amazon-workspaces-web/refs/heads/main/apis.yml
use_cases:
- description: Provide contractors and third-party vendors secure access to internal tools without requiring VPN or device enrollment.
  name: Secure Third-Party Access
- description: Enable bring-your-own-device policies while maintaining security controls over corporate application access.
  name: BYOD Security
- description: Enforce data handling compliance requirements through browser-level controls for regulated industries.
  name: Compliance-Driven Browsing
- description: Provide secure, controlled access to SaaS applications with session recording and data exfiltration prevention.
  name: SaaS Application Security
- description: Create isolated browser environments for development and testing of internal web applications.
  name: Developer Sandbox Environments
---
