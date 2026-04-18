---
api_count: 1
apis:
- description: REST API for managing GitHub Actions workflows, runs, artifacts, and secrets.
  name: GitHub Actions API
  slug: ''
capabilities:
- description: Unified capability for GitHub Actions CI/CD automation combining workflow management, run monitoring, artifact handling, secrets/variables management, and runner administration. Used by DevOps enginee
  name: GitHub Actions CI/CD Automation
  slug: ci-cd-automation
common:
- title: ''
  type: TermsOfService
  url: https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- title: ''
  type: PrivacyPolicy
  url: https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement
- title: ''
  type: RateLimits
  url: https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api
- title: ''
  type: Blog
  url: https://github.blog/category/product/actions/
- title: ''
  type: StatusPage
  url: https://www.githubstatus.com
- title: ''
  type: ChangeLog
  url: https://github.blog/changelog/label/actions/
- title: ''
  type: GettingStarted
  url: https://docs.github.com/en/actions/get-started/quickstart
- title: ''
  type: Authentication
  url: https://docs.github.com/en/rest/overview/authenticating-to-the-rest-api
- title: ''
  type: Support
  url: https://support.github.com
- title: ''
  type: Pricing
  url: https://github.com/pricing
- title: ''
  type: GitHubOrganization
  url: https://github.com/github
- title: ''
  type: Portal
  url: https://docs.github.com/en/rest
- title: ''
  type: Documentation
  url: https://docs.github.com/en/actions
- title: ''
  type: SignUp
  url: https://github.com/signup
- title: ''
  type: Login
  url: https://github.com/login
- title: ''
  type: DeveloperPortal
  url: https://developer.github.com/
- title: ''
  type: Marketplace
  url: https://github.com/marketplace?type=actions
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/github-actions
- title: ''
  type: YouTube
  url: https://www.youtube.com/github
- title: JavaScript SDK
  type: SDK
  url: https://github.com/octokit/octokit.js
- title: Ruby SDK
  type: SDK
  url: https://github.com/octokit/octokit.rb
- title: .NET SDK
  type: SDK
  url: https://github.com/octokit/octokit.net
- title: Go SDK
  type: SDK
  url: https://github.com/google/go-github
- title: ''
  type: CLI
  url: https://cli.github.com/
- title: ''
  type: Quickstart
  url: https://docs.github.com/en/rest/quickstart
- title: ''
  type: Security
  url: https://docs.github.com/en/actions/security-for-github-actions
- title: ''
  type: JSONLD
  url: json-ld/github-actions-context.jsonld
- title: ''
  type: JSONSchema
  url: json-schema/github-actions-workflow-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/github-actions-run-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/github-actions-job-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/github-actions-artifact-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/github-actions-secret-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/github-actions-runner-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/github-actions-variable-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/github-actions-cache-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/github-actions-simple-user-schema.json
- title: CI/CD Automation Capability
  type: Capabilities
  url: capabilities/ci-cd-automation.yaml
- title: Actions API Shared Definition
  type: Capabilities
  url: capabilities/shared/actions.yaml
created: '2024'
description: APIs for GitHub Actions - automation and CI/CD platform.
features:
- Automated CI/CD workflows triggered by repository events
- Matrix builds across multiple OS and language versions
- Reusable workflows and composite actions
- Encrypted secrets and variables at repo, org, and environment scopes
- Self-hosted and GitHub-hosted runner management
- Workflow artifact storage and sharing
- Deployment protection rules and environment approvals
- OIDC integration for cloud provider authentication
- Dependency caching for faster builds
- Runner groups for organizational access control
image: https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png
integrations:
- AWS (via OIDC)
- Azure (via OIDC)
- Google Cloud (via OIDC)
- Docker Hub
- npm
- PyPI
- Slack
- Jira
jsonld:
- class_count: 0
  name: Github Actions Context
  property_count: 0
  slug: github-actions-context
layout: provider
modified: '2026-04-18'
name: GitHub Actions
rules:
- name: GitHub Actions API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: github-actions-spectral-rules
skills: []
slug: github-actions
solutions: []
tags: []
url: https://docs.github.com/en/rest/actions
use_cases:
- Continuous integration and testing on every push or pull request
- Automated deployment to cloud environments
- Scheduled maintenance and cleanup workflows
- Building and publishing container images
- Automated code quality and security scanning
- Release management and artifact publishing
---
