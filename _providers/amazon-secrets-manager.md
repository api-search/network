---
api_count: 1
apis:
- description: The Amazon Secrets Manager API for creating, managing, retrieving, and rotating secrets including database credentials, API keys, and other sensitive configuration.
  name: Amazon Secrets Manager API
  slug: ''
capabilities:
- description: Unified capability for managing application secrets lifecycle including creation, retrieval, rotation, and deletion. Used by DevOps Engineers and Application Developers.
  name: Amazon Secrets Manager Secrets Management
  slug: secrets-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: GettingStarted
  url: https://aws.amazon.com/secrets-manager/getting-started/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/
- title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/secretsmanager/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Pricing
  url: https://aws.amazon.com/secrets-manager/pricing/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/secrets-manager/faqs/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Security
  url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/security.html
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-secrets-manager
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/
- title: ''
  type: SpectralRules
  url: rules/amazon-secrets-manager-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-secrets-manager-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/secrets-management.yaml
- title: ''
  type: JSON-LD
  url: json-ld/amazon-secrets-manager-context.jsonld
- title: ''
  type: JSONSchema
  url: json-schema/amazon-secrets-manager-get-random-password-response-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/amazon-secrets-manager-list-secrets-response-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/amazon-secrets-manager-tag-schema.json
- title: ''
  type: JSONStructure
  url: json-structure/amazon-secrets-manager-get-random-password-response-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/amazon-secrets-manager-list-secrets-response-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/amazon-secrets-manager-rotation-rules-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/amazon-secrets-manager-secret-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/amazon-secrets-manager-secret-value-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/amazon-secrets-manager-tag-structure.json
- title: ''
  type: Example
  url: examples/amazon-secrets-manager-get-random-password-response-example.json
- title: ''
  type: Example
  url: examples/amazon-secrets-manager-list-secrets-response-example.json
- title: ''
  type: Example
  url: examples/amazon-secrets-manager-rotation-rules-example.json
- title: ''
  type: Example
  url: examples/amazon-secrets-manager-secret-example.json
- title: ''
  type: Example
  url: examples/amazon-secrets-manager-secret-value-example.json
- title: ''
  type: Example
  url: examples/amazon-secrets-manager-tag-example.json
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/amazon-secrets-manager.yaml
created: '2024-01-01'
description: Amazon Secrets Manager helps you manage, retrieve, and rotate database credentials, API keys, and other secrets throughout their lifecycle. It provides centralized secrets management with built-in integration for Amazon RDS, Amazon Redshift, and Amazon DocumentDB, enabling automatic rotation of secrets without requiring application changes.
features:
- description: Automatically rotate secrets on a schedule using AWS Lambda rotation functions without changing application code.
  name: Automatic Secret Rotation
- description: Store and manage all secrets in a single, centralized location with fine-grained access controls.
  name: Centralized Secret Storage
- description: Built-in integration with Amazon RDS, Aurora, Redshift, and DocumentDB for automatic credential rotation.
  name: Native Database Integration
- description: Maintain multiple versions of a secret simultaneously to support zero-downtime rotation.
  name: Secret Versioning
- description: Log all secret access and management actions via AWS CloudTrail for compliance and audit purposes.
  name: Audit and Compliance
- description: Share secrets across AWS accounts using resource-based policies.
  name: Cross-Account Access
- description: All secrets are encrypted at rest using AWS KMS keys you control.
  name: Encryption at Rest
- description: Generate cryptographically secure random passwords with configurable complexity requirements.
  name: Random Password Generation
image: ''
integrations:
- description: Native integration for automatic rotation of RDS database credentials.
  name: Amazon RDS
- description: Built-in support for rotating Aurora database master user passwords.
  name: Amazon Aurora
- description: Automatic rotation of Redshift cluster credentials.
  name: Amazon Redshift
- description: Native rotation support for DocumentDB user credentials.
  name: Amazon DocumentDB
- description: Lambda-powered custom rotation functions for any secret type.
  name: AWS Lambda
- description: Audit logging of all Secrets Manager API calls via CloudTrail.
  name: AWS CloudTrail
- description: Encryption of secrets at rest using customer-managed KMS keys.
  name: AWS KMS
- description: Fine-grained access control for secrets using IAM policies and resource-based policies.
  name: AWS IAM
- description: Provision and manage secrets as part of CloudFormation stacks.
  name: AWS CloudFormation
jsonld:
- class_count: 6
  name: Amazon Secrets Manager Context
  property_count: 27
  slug: amazon-secrets-manager-context
layout: provider
modified: '2026-04-19'
name: Amazon Secrets Manager
rules:
- name: Amazon Secrets Manager API Rules
  rule_count: 20
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 10
  slug: amazon-secrets-manager-spectral-rules
skills: []
slug: amazon-secrets-manager
solutions: []
tags:
- AWS
- Configuration
- Credentials
- Rotation
- Secrets
- Security
url: https://aws.amazon.com/secrets-manager/
use_cases:
- description: Automatically rotate and manage database credentials for RDS, Aurora, and other databases.
  name: Database Credential Management
- description: Securely store and retrieve API keys, OAuth tokens, and other third-party service credentials.
  name: API Key Storage
- description: Centralize sensitive application configuration such as connection strings and encryption keys.
  name: Application Configuration
- description: Share service-to-service credentials securely across microservices without embedding in code.
  name: Cross-Service Credentials
- description: Meet compliance requirements like PCI DSS and SOC 2 by enforcing regular credential rotation.
  name: Compliance Secret Rotation
- description: Enforce organizational policies on secret creation, rotation schedules, and access patterns.
  name: Secrets Lifecycle Governance
---
