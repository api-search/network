---
api_count: 1
apis:
- description: The REST API for Bitbucket Cloud allows you to build apps using any language, exposing operations on repositories, pull requests, commits, pipelines, workspaces, projects, webhooks, issues, and users.
  name: Bitbucket Cloud REST API
  slug: bitbucket-cloud-rest-api
capabilities:
- description: Workflow capability for code collaboration using Bitbucket - managing repositories, pull requests, code reviews, and CI/CD pipelines. Used by developers and DevOps engineers.
  name: Bitbucket Code Collaboration
  slug: code-collaboration
common:
- title: ''
  type: Portal
  url: https://developer.atlassian.com/
- title: ''
  type: StatusPage
  url: https://status.atlassian.com/
- title: ''
  type: TermsOfService
  url: https://www.atlassian.com/legal/cloud-terms-of-service
- title: ''
  type: PrivacyPolicy
  url: https://www.atlassian.com/legal/privacy-policy
- title: ''
  type: SignUp
  url: https://bitbucket.org/account/signup/
- title: ''
  type: Blog
  url: https://bitbucket.org/blog/
- title: ''
  type: GitHubOrganization
  url: https://github.com/atlassian
- title: ''
  type: Support
  url: https://support.atlassian.com/bitbucket-cloud/
- title: ''
  type: JSON-LD
  url: json-ld/bitbucket-cloud-rest-api-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/bitbucket-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/code-collaboration.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/bitbucket-vocabulary.yaml
created: '2024-01-01'
description: Bitbucket is a Git-based source code repository hosting service owned by Atlassian offering both commercial plans and free accounts with unlimited private repositories, along with CI/CD pipelines, code reviews via pull requests, and code collaboration tools for development teams.
features:
- description: Host unlimited private and public Git repositories with fine-grained access controls.
  name: Git Repository Hosting
- description: Code review workflows with inline comments, approvals, and merge checks.
  name: Pull Requests
- description: Integrated CI/CD service for building, testing, and deploying code.
  name: Bitbucket Pipelines
- description: Enforce branch restrictions and merge requirements.
  name: Branch Permissions
- description: Receive real-time notifications about repository events.
  name: Webhooks
- description: Built-in issue tracker for managing bugs and feature requests.
  name: Issue Tracking
- description: Track deployments across multiple environments.
  name: Deployment Environments
- description: Search across repositories, code, and pull requests.
  name: Code Search
- description: Share code snippets with version history.
  name: Snippets
image: /assets/icons/bitbucket.png
integrations:
- description: Deep integration with Jira for issue tracking and project management.
  name: Jira Software
- description: Connect Bitbucket with Trello for visual project management.
  name: Trello
- description: Receive Bitbucket notifications in Slack channels.
  name: Slack
- description: Link documentation in Confluence with code in Bitbucket.
  name: Confluence
- description: Deploy to AWS services using Bitbucket Pipelines.
  name: AWS
- description: Deploy to Azure services using Bitbucket Pipelines.
  name: Azure
- description: Deploy to Google Cloud using Bitbucket Pipelines.
  name: Google Cloud
- description: Build and push Docker images using Bitbucket Pipelines.
  name: Docker
jsonld:
- class_count: 4
  name: Bitbucket Cloud Rest Api Context
  property_count: 23
  slug: bitbucket-cloud-rest-api-context
layout: provider
modified: '2026-04-18'
name: Bitbucket
rules:
- name: Bitbucket API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 9
  slug: bitbucket-spectral-rules
skills: []
slug: bitbucket
solutions: []
tags:
- Atlassian
- CI/CD
- Code Collaboration
- Code Review
- DevOps
- Git
- Pull Requests
- Repository Hosting
- Version Control
url: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/apis.yml
use_cases:
- description: Enforce code quality through structured pull request reviews with required approvals.
  name: Code Review Workflows
- description: Automate build, test, and deployment pipelines triggered by code changes.
  name: CI/CD Automation
- description: Enable distributed development teams to collaborate on code with workspaces and projects.
  name: Team Collaboration
- description: Manage releases with deployment tracking and environment promotion.
  name: Release Management
- description: Integrate security scanning into CI/CD pipelines for vulnerability detection.
  name: Security Scanning
---
