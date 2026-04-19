---
api_count: 2
apis:
- description: Akamai API Security provides end-to-end API protection including discovery, posture management, runtime protection, and active testing. It discovers all APIs including shadow and zombie APIs, identifi
  name: Akamai API Security
  slug: api-security
- description: Akamai provides a comprehensive set of REST APIs for managing and configuring their platform services, including API security, CDN, edge computing, and security products. The APIs use the Akamai EdgeG
  name: Akamai APIs
  slug: akamai-apis
capabilities:
- description: Unified workflow for managing Akamai API Security configurations, policies, and threat protection. Covers security posture management, API discovery, and configuration activation for security teams.
  name: Akamai API Security Management
  slug: api-security-management
common:
- title: ''
  type: Website
  url: https://www.akamai.com/products/api-security
- title: ''
  type: Documentation
  url: https://techdocs.akamai.com
- title: ''
  type: Blog
  url: https://www.akamai.com/blog
- title: ''
  type: Pricing
  url: https://www.akamai.com/products/api-security#pricing
- title: ''
  type: Support
  url: https://www.akamai.com/support
- title: ''
  type: Login
  url: https://control.akamai.com
- title: ''
  type: SignUp
  url: https://www.akamai.com/free-trials
- title: ''
  type: GitHubOrganization
  url: https://github.com/akamai
- title: ''
  type: StatusPage
  url: https://www.akamaistatus.com
- title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akamai-technologies
- title: ''
  type: X
  url: https://twitter.com/Akamai
- title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/akamai-api-security/refs/heads/main/rules/akamai-api-security-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/akamai-api-security/refs/heads/main/vocabulary/akamai-api-security-vocabulary.yaml
created: '2026-03-26'
description: Akamai API Security (formerly Noname Security) provides comprehensive API discovery, posture management, and threat protection for organizations across cloud, on-premises, and hybrid environments. The platform continuously discovers and monitors all APIs, identifies vulnerabilities and misconfigurations, detects and responds to API threats in real time, and provides pre-production security testing integrated into CI/CD pipelines.
features:
- description: Automatically discovers all APIs including shadow, zombie, GenAI, LLM, and MCP server APIs across cloud, on-premises, and hybrid environments.
  name: API Discovery
- description: Audits APIs for vulnerabilities and misconfigurations including the full OWASP API Top 10, generating posture findings from runtime incidents.
  name: Posture Management
- description: Uses contextual insights to detect and block API threats including business logic abuse, credential attacks, data scraping, and malicious bots in real time.
  name: Runtime Protection
- description: Runs 200+ dynamic security tests simulating OWASP API Top 10 attacks integrated into CI/CD pipelines without sacrificing development speed.
  name: CI/CD Security Testing
- description: Automatically scans GitHub repositories for OpenAPI specs and adds them to the API library for security analysis and posture assessment.
  name: GitHub Integration
- description: Direct integration with Akamai App and API Protector for blocking API threats detected at runtime.
  name: App and API Protector Integration
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Direct integration for blocking API threats detected by API Security
  name: Akamai App and API Protector
- description: Automatic OpenAPI spec discovery from GitHub repositories
  name: GitHub
- description: Integration with development pipelines for pre-production security testing
  name: CI/CD Pipelines
- description: Export security events to SIEM platforms for centralized monitoring
  name: SIEM
- description: Available on AWS Marketplace for cloud-native deployments
  name: AWS Marketplace
jsonld:
- class_count: 71
  name: Akamai Api Security Context
  property_count: 180
  slug: akamai-api-security-context
layout: provider
modified: '2026-04-19'
name: Akamai API Security
rules:
- name: Akamai API Security API Rules
  rule_count: 23
  severity_counts:
    error: 12
    hint: 0
    info: 0
    warn: 11
  slug: akamai-api-security-spectral-rules
skills: []
slug: akamai-api-security
solutions: []
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
url: https://raw.githubusercontent.com/api-evangelist/akamai-api-security/refs/heads/main/apis.yml
use_cases:
- description: Security teams automatically discover undocumented and shadow APIs across their environment to eliminate blind spots.
  name: Shadow API Discovery
- description: Security engineers assess API posture against OWASP API Top 10 and compliance frameworks to prioritize remediation.
  name: API Vulnerability Assessment
- description: SOC analysts detect and respond to API attacks, data leakage, and suspicious behavior in real time.
  name: Real-Time Threat Detection
- description: Development teams integrate API security testing into CI/CD pipelines to find and fix vulnerabilities before production.
  name: Pre-Production API Testing
- description: Compliance teams assess API security posture against industry frameworks and generate audit-ready reports.
  name: Compliance Reporting
---
