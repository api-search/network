---
api_count: 1
apis:
- description: REST API for Anchore Enterprise providing image analysis, vulnerability scanning, policy evaluation, SBOM generation, subscription management, and reporting endpoints for enterprise container security
  name: Anchore Enterprise API
  slug: anchore-enterprise-api
capabilities:
- description: ''
  name: Anchore Container Security
  slug: anchore-container-security
common:
- title: ''
  type: Portal
  url: https://anchore.com/
- title: ''
  type: Documentation
  url: https://docs.anchore.com/
- title: ''
  type: GettingStarted
  url: https://docs.anchore.com/current/docs/quickstart/
- title: ''
  type: Authentication
  url: https://docs.anchore.com/current/docs/using/api_usage/
- title: ''
  type: GitHubOrganization
  url: https://github.com/anchore
- title: ''
  type: Blog
  url: https://anchore.com/blog/
- title: ''
  type: Support
  url: https://anchore.com/support/
- title: ''
  type: Pricing
  url: https://anchore.com/pricing/
- title: ''
  type: StatusPage
  url: https://status.anchore.com/
- title: ''
  type: TermsOfService
  url: https://anchore.com/terms-of-service/
- title: ''
  type: PrivacyPolicy
  url: https://anchore.com/privacy-policy/
- title: ''
  type: JSONSchema
  url: json-schema/anchore-image-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/anchore-vulnerability-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/anchore-sbom-schema.json
- title: ''
  type: SpectralRules
  url: rules/anchore-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/anchore-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/anchore-enterprise-api-context.jsonld
created: '2026-03-26'
description: Anchore is a container and software supply chain security company providing open source and enterprise tools for vulnerability scanning, SBOM generation, policy enforcement, and continuous compliance. Core open source products include Syft (SBOM generator for container images and filesystems), Grype (vulnerability scanner), and Grant (license scanner). The Anchore Enterprise platform adds policy engines, CI/CD integrations, registry connectors, Kubernetes admission control, and reporting. Anchore supports CycloneDX and SPDX SBOM formats and integrates with Docker, Kubernetes, GitHub Actions, Jenkins, and major cloud registries.
features:
- Container image vulnerability scanning (OS and language packages)
- SBOM generation in CycloneDX and SPDX formats (Syft)
- Policy-based compliance enforcement
- Kubernetes admission controller integration
- CI/CD pipeline integration (GitHub Actions, Jenkins, GitLab)
- Registry connectors (Docker Hub, ECR, GCR, ACR, Harbor)
- License scanning and compliance (Grant)
- Grype vulnerability database with NVD, GitHub Advisory, and custom feeds
- Anchore Enterprise reporting and audit logging
- REST API for image analysis, subscriptions, and notifications
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- GitHub Actions (syft-action, scan-action)
- Kubernetes (anchore-charts, admission controller)
- Docker and OCI registries
- Jenkins pipeline integration
- Harbor registry integration
- Amazon ECR, Google GCR, Azure ACR
- Grype vulnerability database
- CycloneDX and SPDX SBOM standards
jsonld:
- class_count: 0
  name: Anchore Enterprise Api Context
  property_count: 14
  slug: anchore-enterprise-api-context
layout: provider
modified: '2026-04-19'
name: Anchore
rules:
- name: Anchore API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 1
    info: 0
    warn: 4
  slug: anchore-spectral-rules
skills: []
slug: anchore
solutions: []
tags:
- Container Security
- Containers
- SBOM
- Software Supply Chain
- Vulnerability Scanning
url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/apis.yml
use_cases:
- Shift-left container security scanning in CI/CD pipelines
- Generate SBOMs for software supply chain transparency
- Enforce image policies at Kubernetes admission control
- Track vulnerabilities across container registries and deployed images
- License compliance scanning for open source components
- Continuous compliance monitoring for regulated industries
- Developer self-service security scanning via CLI tools
---
