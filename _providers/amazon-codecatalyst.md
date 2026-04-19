---
api_count: 1
apis:
- description: The Amazon CodeCatalyst REST API provides programmatic access to spaces, projects, source repositories, Dev Environments, workflows, workflow runs, and user management. Build integrations, automate pr
  name: Amazon CodeCatalyst API
  slug: amazon-codecatalyst-api
capabilities:
- description: Unified workflow for development teams to collaborate on projects, manage spaces, workflows, and source repositories using Amazon CodeCatalyst.
  name: Amazon CodeCatalyst Developer Collaboration
  slug: amazon-codecatalyst-developer-collaboration
common:
- title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/getting-started-overview.html
- title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/tokens-overview.html
- title: ''
  type: Pricing
  url: https://aws.amazon.com/codecatalyst/pricing/
- title: ''
  type: Console
  url: https://codecatalyst.aws/
- title: ''
  type: Portal
  url: https://aws.amazon.com/codecatalyst/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/
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
  url: https://aws.amazon.com/blogs/devops/
- title: ''
  type: SignUp
  url: https://codecatalyst.aws/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: SpectralRules
  url: rules/amazon-codecatalyst-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-codecatalyst-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-codecatalyst-developer-collaboration.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-codecatalyst-context.jsonld
created: '2026-03-16'
description: Amazon CodeCatalyst is a unified software development service that helps teams collaborate more effectively on software projects. It provides integrated tools for source code management, CI/CD workflows, issue tracking, and cloud-based development environments (Dev Environments). Teams can use CodeCatalyst to accelerate development velocity, standardize workflows, and integrate natively with AWS services and third-party tools.
features:
- description: Cloud-based development environments pre-configured with your project code and tools enabling instant onboarding and eliminating local setup friction.
  name: Dev Environments
- description: Built-in Git repositories for hosting and managing source code with branching, pull requests, and code review capabilities.
  name: Source Repositories
- description: Visual workflow builder for creating automated build, test, and deployment pipelines with native AWS service integrations.
  name: CI/CD Workflows
- description: Integrated issue tracking and project boards for organizing work, tracking bugs, and managing feature development alongside code.
  name: Project Management
- description: Organizational units for grouping projects and managing team membership, billing, and resource access across an organization.
  name: Spaces
- description: Connect to GitHub repositories, Jira, Slack, and other third-party tools to incorporate CodeCatalyst into existing development workflows.
  name: Third-Party Integrations
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Connect GitHub repositories to CodeCatalyst projects and sync code.
  name: GitHub
- description: Link CodeCatalyst issues with Jira for unified project tracking.
  name: Jira
- description: Receive CodeCatalyst notifications and workflow status updates in Slack.
  name: Slack
- description: AI coding assistance integrated into Dev Environments and code reviews.
  name: Amazon Q Developer
- description: Deploy serverless functions as part of CodeCatalyst CI/CD workflows.
  name: AWS Lambda
- description: Deploy containerized applications to ECS from CodeCatalyst pipelines.
  name: Amazon ECS
- description: Deploy infrastructure as code using CloudFormation actions in workflows.
  name: AWS CloudFormation
jsonld:
- class_count: 92
  name: Amazon Codecatalyst Context
  property_count: 74
  slug: amazon-codecatalyst-context
layout: provider
modified: '2026-04-19'
name: Amazon CodeCatalyst
rules:
- name: Amazon CodeCatalyst API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 6
  slug: amazon-codecatalyst-spectral-rules
skills: []
slug: amazon-codecatalyst
solutions: []
tags:
- Amazon
- AWS
- Developer Tools
- CI/CD
- Collaboration
- DevOps
- Source Control
url: https://raw.githubusercontent.com/api-evangelist/amazon-codecatalyst/refs/heads/main/apis.yml
use_cases:
- description: Use Dev Environments to eliminate local development setup time, allowing new developers to be productive within minutes on any project.
  name: Rapid Developer Onboarding
- description: Create and enforce consistent build, test, and deployment workflows across all projects in a space, reducing inconsistency and manual pipeline maintenance.
  name: Standardized CI/CD Pipelines
- description: Enable distributed teams to collaborate on source code through integrated repositories, pull requests, and code review workflows.
  name: Collaborative Code Development
---
