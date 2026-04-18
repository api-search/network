---
api_count: 1
apis:
- description: The primary REST API for interacting with TeamCity server, allowing you to manage builds, projects, build configurations, agents, users, VCS roots, changes, tests, investigations, mutes, cloud infrast
  name: TeamCity REST API
  slug: ''
capabilities: []
common:
- title: ''
  type: GettingStarted
  url: https://www.jetbrains.com/help/teamcity/getting-started-with-teamcity.html
- title: ''
  type: Documentation
  url: https://www.jetbrains.com/help/teamcity/teamcity-documentation.html
- title: ''
  type: Pricing
  url: https://www.jetbrains.com/teamcity/buy/
- title: ''
  type: Blog
  url: https://blog.jetbrains.com/teamcity/
- title: ''
  type: X
  url: https://twitter.com/teamcity
- title: ''
  type: GitHubOrganization
  url: https://github.com/JetBrains
- title: ''
  type: GitHubRepository
  url: https://github.com/JetBrains/teamcity-rest-client
- title: ''
  type: StatusPage
  url: https://teamcity-support.jetbrains.com/hc/en-us/categories/200595559-Known-Issues
- title: ''
  type: Marketplace
  url: https://plugins.jetbrains.com/teamcity
- title: ''
  type: Support
  url: https://www.jetbrains.com/support/teamcity/
- title: ''
  type: ChangeLog
  url: https://www.jetbrains.com/help/teamcity/what-s-new-in-teamcity.html
- title: TeamCity CLI
  type: CLI
  url: https://github.com/JetBrains/teamcity-cli
- title: TeamCity REST Client (Kotlin)
  type: SDK
  url: https://github.com/JetBrains/teamcity-rest-client
- title: Terraform Provider for TeamCity
  type: SDK
  url: https://github.com/JetBrains/terraform-provider-teamcity
created: '2024-01-01'
description: JetBrains TeamCity is a powerful continuous integration and deployment server that helps development teams build, test, and deploy software efficiently. TeamCity provides a comprehensive REST API for automating CI/CD workflows, managing projects, build configurations, agents, and infrastructure.
features:
- description: Define multi-stage build pipelines with dependencies and parallel execution.
  name: Build Pipelines
- description: Create complex build chains with snapshot and artifact dependencies between configurations.
  name: Build Chains
- description: Automatically detect and build feature branches from VCS repositories.
  name: Branch Building
- description: Reusable build configuration templates for standardizing pipeline patterns.
  name: Build Templates
- description: Run builds with local code changes before committing to the repository.
  name: Personal Builds
- description: Dynamically provision build agents in the cloud for elastic scaling.
  name: Cloud Agents
- description: Define build configurations as code using Kotlin DSL.
  name: Kotlin DSL Configuration
- description: Track test history across builds and automatically detect flaky tests.
  name: Test History and Flaky Tests
- description: Assign responsibility for failing builds and tests to team members.
  name: Investigation Management
- description: Cache build dependencies and artifacts for faster subsequent builds.
  name: Build Cache
- description: Aggregate results from multiple build configurations into a single view.
  name: Composite Builds
- description: Complete audit logging of all administrative actions and configuration changes.
  name: Audit Trail
image: https://www.jetbrains.com/teamcity/img/teamcity-logo.svg
integrations:
- description: Pull request building, commit status publishing, and webhook triggers from GitHub.
  name: GitHub
- description: Integration with GitLab repositories for VCS operations and merge request builds.
  name: GitLab
- description: Bitbucket Cloud and Server integration for source code and pull request builds.
  name: Bitbucket
- description: Build and push Docker images as part of CI/CD pipelines.
  name: Docker
- description: Deploy to Kubernetes clusters and use Kubernetes pods as build agents.
  name: Kubernetes
- description: AWS S3 artifact storage, EC2/ECS cloud agents, and CodeDeploy integration.
  name: AWS
- description: Azure cloud agents, Azure DevOps integration, and Azure deployment targets.
  name: Azure
- description: Link builds to Jira issues and track deployments.
  name: Jira
- description: Build notifications and status updates via Slack channels.
  name: Slack
- description: Manage TeamCity infrastructure as code using the official Terraform provider.
  name: Terraform
- description: Secure secrets management integration with HashiCorp Vault.
  name: HashiCorp Vault
- description: Single sign-on authentication via SAML identity providers like Okta and OneLogin.
  name: SAML SSO
- description: NuGet package feed hosting and dependency resolution.
  name: NuGet
- description: Maven build runner and artifact repository integration.
  name: Maven
- description: Gradle build runner with build cache and configuration cache support.
  name: Gradle
- description: Bazel build system support via the TeamCity Bazel plugin.
  name: Bazel
jsonld:
- class_count: 0
  name: Teamcity Rest Api Context
  property_count: 9
  slug: teamcity-rest-api
layout: provider
modified: '2026-04-18'
name: TeamCity
skills: []
slug: teamcity
solutions: []
tags:
- Build Automation
- CI/CD
- Continuous Integration
- Deployment
- DevOps
- Testing
url: https://github.com/api-evangelist/teamcity
use_cases:
- description: Automatically build and test code on every commit or pull request.
  name: Continuous Integration
- description: Deploy applications to staging and production environments automatically.
  name: Continuous Deployment
- description: Build and test across Linux, Windows, and macOS using diverse agent pools.
  name: Multi-Platform Builds
- description: Manage CI/CD for monorepos with selective triggering based on changed paths.
  name: Monorepo CI
- description: Orchestrate build and deploy pipelines for microservices architectures.
  name: Microservices Pipelines
- description: Manage release branches, versioning, and deployment gates.
  name: Release Management
- description: Validate Terraform, Kubernetes, and other IaC configurations in CI pipelines.
  name: Infrastructure as Code Testing
- description: Build, test, and distribute mobile applications for iOS and Android.
  name: Mobile App CI/CD
- description: Maintain audit trails and enforce build policies for regulatory compliance.
  name: Compliance and Audit
---
