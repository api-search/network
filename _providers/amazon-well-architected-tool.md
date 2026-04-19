---
api_count: 1
apis:
- description: The AWS Well-Architected Tool API provides programmatic access to create and manage workloads, lenses, milestones, profiles, review templates, and review reports. It enables integration of the Well-Ar
  name: AWS Well-Architected Tool API
  slug: aws-well-architected-tool-api
capabilities:
- description: Unified workflow for architecture governance using the AWS Well-Architected Tool. Enables cloud architects and governance teams to manage workloads, run lens reviews, track answers, create milestones,
  name: Amazon Well-Architected Tool Architecture Governance
  slug: architecture-governance
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/well-architected-tool/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/wellarchitected/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Login
  url: https://aws.amazon.com/console/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: GitHubRepository
  url: https://github.com/aws-samples/custom-lens-wa-hub
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-well-architected-tool-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-well-architected-tool-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/architecture-governance.yaml
created: '2026-03-16'
description: 'The AWS Well-Architected Tool helps you review your workloads and compare them to the latest AWS architectural best practices. It provides a consistent process for evaluating architectures and implementing designs that scale over time across five pillars: operational excellence, security, reliability, performance efficiency, and cost optimization. The tool offers lens catalogs, custom lenses, profiles, review templates, and API-driven extensibility for integration into governance workflows.'
features:
- description: Expert-authored review lenses from AWS covering diverse technology and industry-specific pillars, continuously refreshed with latest best practices.
  name: Lens Catalog
- description: Create organization-specific lenses that combine internal best practices with AWS guidance, shareable with up to 300 IAM users or across AWS Organizations.
  name: Custom Lenses
- description: Pre-define business goals to auto-generate prioritized review questions tailored to your workload context.
  name: Profiles
- description: Standardize answers across multiple workloads to ensure consistent architectural reviews at scale.
  name: Review Templates
- description: Share workloads and custom lenses with IAM users or integrate with AWS Organizations for organization-wide access and visibility.
  name: Enhanced Collaboration
- description: Native integration with AWS Trusted Advisor and AWS Service Catalog AppRegistry to reduce manual review effort.
  name: Service Integration
- description: Robust APIs allow extending Well-Architected functionality into existing architecture governance processes, applications, and workflows.
  name: API-Driven Extensibility
- description: Save milestones, implement improvements, and measure progress over time with point-in-time snapshots of workload review state.
  name: Milestone Tracking
- description: Available in GovCloud (US) with FedRAMP compliance for organizations with stringent regulatory requirements.
  name: Compliance and Regulatory Support
- description: Generate consolidated reports across workloads for governance and executive visibility into architectural risk posture.
  name: Consolidated Reporting
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Integration with AWS Trusted Advisor provides automated checks that complement manual Well-Architected review processes.
  name: AWS Trusted Advisor
- description: AppRegistry integration enables linking Well-Architected workloads to application metadata for richer governance context.
  name: AWS Service Catalog AppRegistry
- description: Organization-level sharing of workloads and custom lenses for enterprise-wide architectural governance programs.
  name: AWS Organizations
- description: Fine-grained access control via AWS IAM for workload sharing and reviewer management within the tool.
  name: AWS IAM
- description: Workloads can be associated with CloudFormation stacks for automated resource discovery and architecture documentation.
  name: AWS CloudFormation
jsonld:
- class_count: 146
  name: Amazon Well Architected Tool Context
  property_count: 139
  slug: amazon-well-architected-tool-context
layout: provider
modified: '2026-04-19'
name: Amazon Well-Architected Tool
rules:
- name: Amazon Well-Architected Tool API Rules
  rule_count: 25
  severity_counts:
    error: 9
    hint: 0
    info: 5
    warn: 11
  slug: amazon-well-architected-tool-spectral-rules
skills: []
slug: amazon-well-architected-tool
solutions: []
tags:
- Architecture
- AWS
- Best Practices
- Cloud Governance
- Well-Architected
- Workloads
url: https://raw.githubusercontent.com/api-evangelist/amazon-well-architected-tool/refs/heads/main/apis.yml
use_cases:
- description: Evaluate cloud workload architecture quality against AWS best practices across the five Well-Architected pillars.
  name: Architecture Reviews and Governance
- description: Use review templates to standardize architectural answers and enforce consistent governance across multiple workloads and teams.
  name: Multi-Workload Standardization
- description: Apply industry-specific and technology-specific lenses from the lens catalog to assess specialized workloads.
  name: Industry-Specific Best Practice Implementation
- description: Evaluate workloads for FedRAMP, GovCloud, and other regulatory compliance requirements through targeted lenses.
  name: Regulatory Compliance Assessment
- description: Integrate Well-Architected reviews into CI/CD workflows and automation pipelines for continuous architecture assessment.
  name: DevOps Pipeline Integration
- description: Share workloads with reviewers and stakeholders to facilitate collaborative architectural decision-making across teams.
  name: Cross-Team Architectural Alignment
- description: Use the sustainability pillar to minimize environmental impact and meet organizational sustainability commitments.
  name: Sustainability Goal Realization
---
