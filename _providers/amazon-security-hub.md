---
api_count: 1
apis:
- description: The AWS Security Hub API provides programmatic access to manage centralized security findings across your AWS environment. It enables developers to import and manage security findings, configure secur
  name: AWS Security Hub API
  slug: ''
capabilities:
- description: Unified capability for cloud security posture management including findings aggregation, compliance standards monitoring, and security insights. Used by Cloud Security Engineers and SOC Analysts.
  name: Amazon Security Hub Cloud Security Posture
  slug: cloud-security-posture
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: GettingStarted
  url: https://aws.amazon.com/security-hub/getting-started/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/securityhub/
- title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/securityhub/latest/APIReference/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/securityhub/
- title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- title: ''
  type: Pricing
  url: https://aws.amazon.com/security-hub/pricing/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/security-hub/faqs/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-security-hub
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: SpectralRules
  url: rules/amazon-security-hub-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-security-hub-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/cloud-security-posture.yaml
- title: ''
  type: JSON-LD
  url: json-ld/amazon-security-hub-context.jsonld
- title: ''
  type: JSONStructure
  url: json-structure/amazon-security-hub-finding-structure.json
- title: ''
  type: Example
  url: examples/amazon-security-hub-finding-example.json
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/amazon-security-hub.yaml
created: '2024-01-15'
description: AWS Security Hub is a cloud security posture management service that provides a comprehensive view of your security state across AWS accounts. It aggregates, organizes, and prioritizes security findings from multiple AWS services and third-party tools, enabling centralized security monitoring, compliance checking, and automated remediation workflows.
features:
- description: Aggregate security findings from across multiple AWS accounts and regions into a single pane of glass.
  name: Multi-Account Findings Aggregation
- description: Standardized JSON format for all security findings enabling consistent analysis and automation.
  name: AWS Security Finding Format (ASFF)
- description: Automated compliance checks against CIS AWS Foundations, PCI DSS, NIST, SOC 2, and AWS Foundational Security Best Practices.
  name: Built-in Compliance Standards
- description: Ingest findings from 80+ third-party security partners including CrowdStrike, Palo Alto Networks, and Splunk.
  name: Third-Party Integrations
- description: Trigger automated remediation via Amazon EventBridge and AWS Security Hub automated response and remediation.
  name: Automated Remediation
- description: Correlated views of security findings to highlight areas needing attention.
  name: Security Insights
- description: Create custom actions to send findings to ticketing, chat, and SOAR platforms.
  name: Custom Actions
- description: Aggregate findings across multiple AWS regions into a designated aggregation region.
  name: Cross-Region Aggregation
image: ''
integrations:
- description: Native integration to ingest GuardDuty threat detection findings.
  name: Amazon GuardDuty
- description: Aggregate Inspector vulnerability assessment findings.
  name: Amazon Inspector
- description: Ingest Macie sensitive data discovery findings.
  name: Amazon Macie
- description: Integration with Config rules for configuration compliance findings.
  name: AWS Config
- description: Trigger automated remediation and notification workflows based on findings.
  name: Amazon EventBridge
- description: Execute custom remediation actions in response to security findings.
  name: AWS Lambda
- description: Enable Security Hub across all accounts in an AWS Organization.
  name: AWS Organizations
- description: Third-party integration for endpoint detection and response findings.
  name: CrowdStrike
- description: Export Security Hub findings to Splunk SIEM for advanced analysis.
  name: Splunk
- description: Ingest Prisma Cloud and other Palo Alto findings via Security Hub integration.
  name: Palo Alto Networks
jsonld:
- class_count: 1
  name: Amazon Security Hub Context
  property_count: 15
  slug: amazon-security-hub-context
layout: provider
modified: '2026-04-19'
name: Amazon Security Hub
rules:
- name: Amazon Security Hub API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 8
  slug: amazon-security-hub-spectral-rules
skills: []
slug: amazon-security-hub
solutions: []
tags:
- AWS
- Compliance
- Monitoring
- Security
url: https://aws.amazon.com/security-hub/
use_cases:
- description: Continuously monitor your AWS environment for security misconfigurations and compliance gaps.
  name: Cloud Security Posture Management
- description: Automate compliance checks and generate reports for CIS, PCI DSS, NIST, and other frameworks.
  name: Compliance Reporting
- description: Centralize security monitoring across dozens or hundreds of AWS accounts in an organization.
  name: Multi-Account Security Operations
- description: Aggregate findings from GuardDuty, Inspector, Macie, and third-party tools in one place.
  name: Threat Detection Aggregation
- description: Trigger automated remediation workflows when critical findings are detected.
  name: Automated Incident Response
- description: Replace multiple point solutions with centralized finding aggregation and normalized data.
  name: Security Tool Consolidation
---
