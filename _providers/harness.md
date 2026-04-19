---
api_count: 13
apis:
- description: The Harness Platform API provides access to core platform resources including projects, organizations, connectors, secrets, users, roles, resource groups, service accounts, variables, pipelines, trigg
  name: Harness Platform API
  slug: platform-api
- description: The Harness CI module helps build faster with features including code building, testing, dependency management, artifact uploads, and build monitoring with AI-powered Test Intelligence.
  name: Harness Continuous Integration API
  slug: ci-api
- description: The Harness CD and GitOps module automates all steps necessary to get changes into production with APIs for pipelines, execution, input sets, triggers, and approvals supporting multi-cloud deployments
  name: Harness Continuous Delivery and GitOps API
  slug: cd-api
- description: APIs to create and manage feature flags, targets, target groups, and tags for feature release management, performance monitoring, and A/B testing.
  name: Harness Feature Management and Experimentation API
  slug: feature-flags-api
- description: Cloud cost management APIs for cost recommendations, AutoStopping rules, commitment orchestration, cost categories, anomaly detection, asset governance, and BI dashboards.
  name: Harness Cloud Cost Management API
  slug: ccm-api
- description: APIs for chaos engineering, load testing, and disaster recovery testing including chaos experiments, probes, actions, faults, and resilience scoring.
  name: Harness Chaos Engineering API
  slug: chaos-api
- description: APIs for security vulnerability detection with over 40 scanner integrations for running scans, viewing results, and enforcing security policies across the software delivery lifecycle.
  name: Harness Security Testing Orchestration API
  slug: sto-api
- description: Backstage-powered Internal Developer Portal APIs for software catalog management, self-service workflows, scorecards, and developer experience.
  name: Harness Internal Developer Portal API
  slug: idp-api
- description: Source control management APIs for repositories, collaboration tools, pull requests, and pipeline integration.
  name: Harness Code Repository API
  slug: code-repo-api
- description: APIs for managing service level objectives, monitored services, and service dashboards for balancing feature velocity with reliability.
  name: Harness Service Reliability Management API
  slug: srm-api
- description: APIs for defining, deploying, and managing infrastructure across environments with Terraform and IaC tool integration.
  name: Harness Infrastructure as Code Management API
  slug: iacm-api
- description: APIs for SBOM generation, artifact integrity verification, and policy enforcement for software supply chain security and compliance.
  name: Harness Supply Chain Security API
  slug: ssca-api
- description: APIs for accessing engineering metrics and analytics data to improve engineering productivity, efficiency, and alignment.
  name: Harness Software Engineering Insights API
  slug: sei-api
common:
- title: ''
  type: Portal
  url: https://developer.harness.io/docs/
- title: ''
  type: Documentation
  url: https://apidocs.harness.io
- title: ''
  type: GettingStarted
  url: https://developer.harness.io/docs/platform/automation/api/api-quickstart/
- title: ''
  type: Authentication
  url: https://developer.harness.io/docs/platform/automation/api/add-and-manage-api-keys/
- title: ''
  type: Pricing
  url: https://www.harness.io/pricing
- title: ''
  type: SignUp
  url: https://app.harness.io/auth/
- title: ''
  type: Blog
  url: https://www.harness.io/blog
- title: ''
  type: Support
  url: https://www.harness.io/support
- title: ''
  type: StatusPage
  url: https://status.harness.io
- title: ''
  type: ChangeLog
  url: https://developer.harness.io/release-notes/
- title: ''
  type: TermsOfService
  url: https://www.harness.io/legal/website-terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://www.harness.io/legal/privacy
- title: ''
  type: GitHubOrganization
  url: https://github.com/harness
- title: ''
  type: Training
  url: https://developer.harness.io/university/
- title: ''
  type: Security
  url: https://www.harness.io/security
created: '2026-01-02'
description: Harness is an AI-powered software delivery platform that automates and accelerates the entire software development lifecycle from code to production. The platform provides intelligent automation across DevOps, testing and resilience, security and compliance, and cost optimization, helping engineering teams ship code faster, safer, and smarter as they scale.
features:
- description: Intelligent automation with Harness AI for test intelligence, deployment verification, and cost optimization.
  name: AI-Powered Automation
- description: Visual pipeline builder with conditional logic, parallel execution, and approval gates.
  name: Pipeline Orchestration
- description: Declarative GitOps deployments with Argo CD integration for Kubernetes workloads.
  name: GitOps Deployments
- description: Progressive feature rollouts with targeting, experimentation, and A/B testing capabilities.
  name: Feature Flag Management
- description: FinOps capabilities including AutoStopping, commitment orchestration, and cost anomaly detection.
  name: Cloud Cost Optimization
- description: Resilience testing with chaos experiments, load testing, and disaster recovery validation.
  name: Chaos Engineering
- description: Automated security scanning with 40+ scanner integrations and policy enforcement.
  name: Security Testing Orchestration
- description: Backstage-powered developer portal for software catalog, self-service workflows, and scorecards.
  name: Internal Developer Portal
image: /assets/icons/harness.png
integrations:
- description: Source code management, GitHub Actions, and GitHub App integration for CI/CD workflows.
  name: GitHub
- description: Native Kubernetes deployment support with Helm, Kustomize, and GitOps.
  name: Kubernetes
- description: Multi-service AWS integration including ECS, EKS, Lambda, S3, and CloudFormation.
  name: AWS
- description: Azure DevOps, AKS, Azure Functions, and Azure Resource Manager integration.
  name: Azure
- description: Google Cloud integration with GKE, Cloud Run, Cloud Functions, and Cloud Build.
  name: GCP
- description: Infrastructure as Code management with Terraform plan, apply, and state management.
  name: Terraform
- description: Issue tracking integration for deployment approvals, change management, and traceability.
  name: Jira
- description: Notifications and approval workflows within Slack channels.
  name: Slack
jsonld:
- class_count: 4
  name: Harness Context
  property_count: 7
  slug: harness-context
layout: provider
modified: '2026-04-18'
name: Harness
rules:
- name: Harness API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 3
  slug: harness-spectral-rules
skills: []
slug: harness
solutions: []
tags:
- DevOps
- GitOps
- Internal Developer Portal
- Lifecycle
- Software Delivery
url: https://raw.githubusercontent.com/api-evangelist/harness/refs/heads/main/apis.yml
use_cases:
- description: Automate build, test, and deploy workflows across multi-cloud and hybrid environments.
  name: CI/CD Pipeline Automation
- description: Roll out features progressively with feature flags, canary deployments, and blue-green strategies.
  name: Progressive Feature Delivery
- description: Optimize cloud spend with automated cost recommendations, idle resource detection, and budget alerts.
  name: Cloud Cost Management
- description: Enforce security policies with automated scanning, SBOM generation, and supply chain verification.
  name: Security Compliance
- description: Build internal developer platforms with self-service workflows, templates, and software catalogs.
  name: Platform Engineering
- description: Manage SLOs, monitor service health, and validate resilience with chaos engineering.
  name: SRE and Reliability
---
