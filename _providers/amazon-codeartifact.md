---
api_count: 1
apis:
- description: The Amazon CodeArtifact REST API enables programmatic management of artifact repositories, domains, packages, and package versions. Manage domains and repositories, control permissions policies, publi
  name: Amazon CodeArtifact API
  slug: amazon-codeartifact-api
capabilities:
- description: Unified workflow for DevOps teams to manage artifact repositories, publish packages, control access, and govern software supply chains using Amazon CodeArtifact.
  name: Amazon CodeArtifact Package Management
  slug: amazon-codeartifact-package-management
common:
- title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/codeartifact/latest/ug/getting-started.html
- title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html
- title: ''
  type: Pricing
  url: https://aws.amazon.com/codeartifact/pricing/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/codesuite/codeartifact/start
- title: ''
  type: Portal
  url: https://aws.amazon.com/codeartifact/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/codeartifact/latest/ug/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/devops/category/developer-tools/amazon-codeartifact/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/gp/aws/developer/registration/index.html
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: SpectralRules
  url: rules/amazon-codeartifact-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-codeartifact-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-codeartifact-package-management.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-codeartifact-context.jsonld
created: '2026-03-16'
description: Amazon CodeArtifact is a fully managed, secure artifact repository service that helps organizations store, publish, and share software packages used in their software development process. CodeArtifact works with popular build tools and package managers including npm, yarn, pip, twine, Maven, Gradle, NuGet, and more. It supports Cargo, generic, Maven, npm, NuGet, PyPI, Ruby, and Swift package formats and integrates natively with AWS IAM, AWS KMS, AWS CloudTrail, and Amazon EventBridge.
features:
- description: Supports Cargo, generic, Maven, npm, NuGet, PyPI, Ruby, and Swift package formats in polyglot repositories that can hold any supported package type in a single repository.
  name: Multi-Format Package Support
- description: Connect repositories to public sources including npmjs, PyPI, Maven Central, NuGet Gallery, and RubyGems.org to proxy and cache open-source dependencies on demand.
  name: Public Repository Integration
- description: Aggregate multiple repositories into a domain to apply organizational policies, manage encryption, and share packages across development teams.
  name: Domain-Based Organization
- description: Create upstream relationships between repositories so downstream repositories can transparently access packages from upstream sources, effectively merging their contents.
  name: Upstream Repositories
- description: Apply configuration to multiple packages using package groups with pattern matching. Use origin controls to block or allow ingestion or publishing of new package versions against dependency substitution attacks.
  name: Package Groups and Origin Controls
- description: Generate temporary authorization tokens (up to 12 hours) for secure authentication with package managers without long-lived credentials.
  name: Authorization Token Generation
- description: Control access to domains and repositories using AWS Identity and Access Management for fine-grained permissions policies.
  name: AWS IAM Integration
- description: All assets and metadata in a domain are encrypted with the same AWS KMS key, supporting both AWS managed and customer managed keys.
  name: AWS KMS Encryption
- description: Track package usage and access across your organization with full audit logging via AWS CloudTrail.
  name: AWS CloudTrail Integration
- description: Automate package governance workflows and trigger actions on package events using Amazon EventBridge.
  name: Amazon EventBridge Integration
- description: Access CodeArtifact repositories from within a VPC without exposing traffic to the public internet using AWS PrivateLink endpoints.
  name: AWS PrivateLink Support
- description: Multi-Availability Zone operation with redundant package asset storage across Amazon S3 and DynamoDB, fully managed with automatic scaling.
  name: High Availability Storage
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Fine-grained access control for domains, repositories, and package operations.
  name: AWS IAM
- description: Encryption key management for all package assets and metadata stored in a domain.
  name: AWS KMS
- description: Audit logging for all CodeArtifact API calls and package access events.
  name: AWS CloudTrail
- description: Event-driven automation for package governance workflows and notifications.
  name: Amazon EventBridge
- description: Private network connectivity to CodeArtifact from within a VPC.
  name: AWS PrivateLink
- description: Public upstream connection for npm package proxying and caching.
  name: npm Registry (npmjs.com)
- description: Public upstream connection for Python package proxying and caching.
  name: PyPI (pypi.org)
- description: Public upstream connection for Java/Maven package proxying and caching.
  name: Maven Central
- description: Public upstream connection for .NET package proxying and caching.
  name: NuGet Gallery (nuget.org)
- description: Public upstream connection for Ruby gem proxying and caching.
  name: RubyGems.org
- description: Public upstream connection for Rust/Cargo package proxying and caching.
  name: crates.io
- description: Integrate CodeArtifact with GitHub Actions CI/CD workflows for package management.
  name: GitHub Actions
- description: Use CodeArtifact as the package source in AWS CodeBuild build projects.
  name: AWS CodeBuild
- description: Incorporate package publishing and consumption into AWS CodePipeline deployment pipelines.
  name: AWS CodePipeline
jsonld:
- class_count: 106
  name: Amazon Codeartifact Context
  property_count: 76
  slug: amazon-codeartifact-context
layout: provider
modified: '2026-04-19'
name: Amazon CodeArtifact
rules:
- name: Amazon CodeArtifact API Rules
  rule_count: 23
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 10
  slug: amazon-codeartifact-spectral-rules
skills: []
slug: amazon-codeartifact
solutions: []
tags:
- Amazon
- AWS
- Artifact Repository
- Package Management
- DevOps
- Software Supply Chain
- npm
- Maven
- PyPI
- NuGet
url: https://raw.githubusercontent.com/api-evangelist/amazon-codeartifact/refs/heads/main/apis.yml
use_cases:
- description: Share proprietary software components and internal libraries between multiple applications and development teams within an organization without managing your own artifact storage infrastructure.
  name: Internal Package Distribution
- description: Proxy and cache open-source packages from public registries to ensure build reproducibility and availability even when upstream registries experience downtime.
  name: Open-Source Dependency Caching
- description: Control which packages developers can use with package origin controls to protect against dependency confusion and substitution attacks.
  name: Software Supply Chain Security
- description: Apply organizational policies across multiple repositories in a domain and audit package consumption across development teams using CloudTrail and EventBridge.
  name: Multi-Team Package Governance
- description: Integrate with CI/CD systems using native package manager support (npm, Maven, pip, NuGet) to fetch and publish packages as part of automated build and release workflows.
  name: CI/CD Pipeline Integration
---
