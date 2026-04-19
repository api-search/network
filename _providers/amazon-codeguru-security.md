---
api_count: 1
apis:
- description: The Amazon CodeGuru Security REST API.
  name: Amazon CodeGuru Security API
  slug: amazon-codeguru-security-api
capabilities:
- description: Unified workflow for security and DevOps teams to create security scans, retrieve findings, track vulnerabilities by severity, and manage remediation using Amazon CodeGuru Security.
  name: Amazon CodeGuru Security Application Security Scanning
  slug: amazon-codeguru-security-security-scanning
common:
- title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/codeguru/security
- title: ''
  type: Pricing
  url: https://aws.amazon.com/codegurusecurity/pricing/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/codegurusecurity/
- title: ''
  type: Portal
  url: https://aws.amazon.com/codegurusecurity/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/codegurusecurity/
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
  url: https://portal.aws.amazon.com/gp/aws/developer/registration/index.html
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: SpectralRules
  url: rules/amazon-codeguru-security-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-codeguru-security-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-codeguru-security-security-scanning.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-codeguru-security-context.jsonld
created: '2026-03-16'
description: Amazon CodeGuru Security is a static application security testing (SAST) service that uses machine learning to detect security vulnerabilities in your code. It identifies vulnerabilities such as injection flaws, data exposure risks, and infrastructure-as-code misconfigurations, and provides actionable remediation guidance to help developers fix security issues quickly.
features:
- description: Analyze source code for security vulnerabilities without running the application using machine learning-powered SAST.
  name: Static Application Security Testing
- description: Detect security issues in Java, Python, JavaScript, TypeScript, C, C++, C#, Go, Ruby, and Kotlin code.
  name: Multi-Language Support
- description: Detect security misconfigurations in CloudFormation, Terraform, CDK, and other IaC templates.
  name: Infrastructure-as-Code Scanning
- description: Classify findings by severity (Critical, High, Medium, Low, Informational) to help prioritize remediation.
  name: Severity Classification
- description: Provide detailed remediation recommendations including suggested code fixes for each identified vulnerability.
  name: Remediation Guidance
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Run security scans as part of CodeBuild build projects for CI/CD integration.
  name: AWS CodeBuild
- description: Add CodeGuru Security scanning to GitHub Actions workflows.
  name: GitHub Actions
- description: Send security findings to Security Hub for centralized security management.
  name: AWS Security Hub
- description: Store and retrieve code bundles for security scanning from S3.
  name: Amazon S3
jsonld:
- class_count: 49
  name: Amazon Codeguru Security Context
  property_count: 70
  slug: amazon-codeguru-security-context
layout: provider
modified: '2026-04-19'
name: Amazon CodeGuru Security
rules:
- name: Amazon CodeGuru Security API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 4
  slug: amazon-codeguru-security-spectral-rules
skills: []
slug: amazon-codeguru-security
solutions: []
tags:
- Amazon
- AWS
- Security
- SAST
- Code Analysis
- DevSecOps
- Developer Tools
url: https://raw.githubusercontent.com/api-evangelist/amazon-codeguru-security/refs/heads/main/apis.yml
use_cases:
- description: Integrate security scanning into CI/CD pipelines to detect vulnerabilities before code reaches production.
  name: DevSecOps Integration
- description: Run security scans on existing codebases to identify and remediate vulnerabilities for compliance audits.
  name: Security Audit and Compliance
- description: Scan infrastructure-as-code templates for security misconfigurations before provisioning cloud resources.
  name: IaC Security Validation
---
