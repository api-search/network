---
api_count: 3
apis:
- description: The 1Password Connect Server API provides secure access to 1Password items and vaults in your company's apps and cloud infrastructure through a private REST API. Connect Servers bridge the gap between
  name: 1Password Connect Server API
  slug: 1password-connect-api
- description: The 1Password Events API provides programmatic access to event data generated within a 1Password account. It enables security teams and administrators to retrieve sign-in attempts, item usage records,
  name: 1Password Events API
  slug: 1password-events-api
- description: You can use the 1Password Partnership API to manage the provisioning and deprovisioning of third-party partner billing accounts for your customers. The API supports partner billing accounts for 1Passw
  name: 1Password Partnership API
  slug: 1password-partnership-api
capabilities:
- description: Unified secrets management and security monitoring workflow for 1Password. Combines the Connect Server API (vault and item management), Events API (audit log and sign-in monitoring), and Partnership A
  name: 1Password Secrets Management
  slug: 1password-secrets-management
common:
- title: ''
  type: Website
  url: https://1password.com/
- title: ''
  type: Portal
  url: https://developer.1password.com/
- title: ''
  type: Documentation
  url: https://developer.1password.com/docs/
- title: ''
  type: GettingStarted
  url: https://developer.1password.com/docs/get-started/
- title: ''
  type: Authentication
  url: https://developer.1password.com/docs/connect/connect-api-reference/#authentication
- title: Official SDKs
  type: SDK
  url: https://developer.1password.com/docs/sdks/
- title: Python SDK
  type: SDK
  url: https://pypi.org/project/onepassword-sdk/
- title: JavaScript SDK
  type: SDK
  url: https://www.npmjs.com/package/@1password/sdk
- title: Go SDK
  type: SDK
  url: https://pkg.go.dev/github.com/1Password/onepassword-sdk-go
- title: Connect Python SDK
  type: SDK
  url: https://pypi.org/project/onepassword-connect-sdk/
- title: Connect Node.js SDK
  type: SDK
  url: https://www.npmjs.com/package/@1password/connect
- title: Connect Go SDK
  type: SDK
  url: https://pkg.go.dev/github.com/1Password/connect-sdk-go
- title: 1Password CLI
  type: CLI
  url: https://developer.1password.com/docs/cli/
- title: ''
  type: Blog
  url: https://blog.1password.com/
- title: ''
  type: Support
  url: https://support.1password.com/
- title: ''
  type: PrivacyPolicy
  url: https://1password.com/legal/privacy/
- title: ''
  type: TermsOfService
  url: https://1password.com/legal/terms-of-service/
- title: ''
  type: SignUp
  url: https://start.1password.com/sign-up/
- title: ''
  type: ChangeLog
  url: https://developer.1password.com/docs/events-api/changelog/
- title: ''
  type: GitHubOrganization
  url: https://github.com/1Password
- title: ''
  type: SpectralRules
  url: rules/1password-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/1password-secrets-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/1password-vocabulary.yaml
created: '2025-02-08'
description: 1Password is a password manager that helps individuals and businesses securely store and manage passwords, credentials, and sensitive information. The platform provides a Connect Server API for programmatic secrets management, an Events API for security monitoring and audit logging, and a Partnership API for managing partner billing accounts.
features:
- description: Programmatic access to 1Password vaults and items via Connect Server API
  name: Secrets Management
- description: Real-time audit log streaming of sign-in events, item usage, and audit trails
  name: Security Monitoring
- description: Provision and deprovision 1Password accounts for partner customers
  name: Partner Billing Management
- description: Official SDKs for Python, JavaScript/TypeScript, Go, and Connect-specific clients
  name: SDKs
- description: 1Password CLI for command-line secrets management and automation
  name: CLI
- description: Kubernetes operator and secrets injector for cloud-native deployments
  name: Kubernetes Integration
- description: Terraform provider to manage 1Password vault items as infrastructure
  name: Terraform Provider
- description: Load secrets from 1Password directly into GitHub Actions CI/CD pipelines
  name: GitHub Actions
image: /assets/icons/1password.png
integrations:
- description: Native integration via operator and secrets injector for Kubernetes deployments
  name: Kubernetes
- description: Terraform provider for managing 1Password items as infrastructure resources
  name: Terraform
- description: Ansible collection for 1Password Connect integration
  name: Ansible
- description: GitHub Actions to load and install 1Password secrets in CI/CD workflows
  name: GitHub Actions
- description: Events API Splunk integration for security event streaming
  name: Splunk
- description: Vault plugin for 1Password Connect secrets retrieval
  name: HashiCorp Vault
- description: Official Helm charts for deploying 1Password Connect on Kubernetes
  name: Helm Charts
jsonld:
- class_count: 15
  name: 1Password Connect Context
  property_count: 46
  slug: 1password-connect-context
- class_count: 0
  name: 1Password Context
  property_count: 8
  slug: 1password-context
- class_count: 13
  name: 1Password Events Context
  property_count: 43
  slug: 1password-events-context
- class_count: 4
  name: 1Password Partnership Context
  property_count: 6
  slug: 1password-partnership-context
layout: provider
modified: '2026-04-19'
name: 1Password
rules:
- name: 1Password API Rules
  rule_count: 30
  severity_counts:
    error: 13
    hint: 0
    info: 6
    warn: 11
  slug: 1password-spectral-rules
skills: []
slug: 1password
solutions: []
tags:
- Password Manager
- Passwords
- Security
- Secrets
url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/apis.yml
use_cases:
- description: Inject secrets from 1Password into applications and containers at runtime
  name: Secrets Injection
- description: Stream and analyze sign-in events and item usage for security incident response
  name: Security Audit
- description: Export audit trails for SOC2, GDPR, and other compliance frameworks
  name: Compliance Reporting
- description: Securely provide secrets to CI/CD pipelines without hardcoding credentials
  name: CI/CD Secrets
- description: Manage secrets as part of Terraform or Ansible automation workflows
  name: Infrastructure as Code
- description: Automate provisioning of 1Password accounts for partner customer bases
  name: Partner Account Provisioning
---
