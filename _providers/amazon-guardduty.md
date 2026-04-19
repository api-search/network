---
api_count: 1
apis:
- description: The Amazon GuardDuty API provides programmatic access to manage detectors, findings, filters, trusted IP sets, and threat intelligence for continuous threat detection across AWS accounts and workloads
  name: Amazon GuardDuty API
  slug: amazon-guardduty-api
capabilities:
- description: Workflow capability for security teams using Amazon GuardDuty for AWS threat detection and response. Covers finding management, detector configuration, threat intelligence integration, and automated r
  name: Amazon GuardDuty Threat Detection
  slug: amazon-guardduty-threat-detection
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/guardduty/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/guardduty/
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
  type: Blog
  url: https://aws.amazon.com/blogs/security/tag/amazon-guardduty/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/guardduty/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-guardduty-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-guardduty-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-guardduty-threat-detection.yaml
created: '2024-01-15'
description: Amazon GuardDuty is an intelligent threat detection service that continuously monitors your AWS accounts, workloads, and data for malicious activity. It uses machine learning, anomaly detection, and integrated threat intelligence to identify and prioritize potential threats to your AWS environment.
features:
- description: Uses ML and anomaly detection to identify threats without manual configuration or rule management.
  name: Intelligent Threat Detection
- description: Incorporates curated threat intelligence feeds from AWS, CrowdStrike, and Proofpoint for enhanced detection.
  name: Integrated Threat Intelligence
- description: Monitor all accounts in an AWS Organization from a central administrator account.
  name: Multi-Account Support
- description: Analyzes CloudTrail, VPC Flow Logs, DNS logs, and S3 access logs 24/7 without performance impact.
  name: Continuous Monitoring
- description: Automatically prioritizes findings by severity (Low, Medium, High) for efficient response.
  name: Finding Prioritization
- description: Scans EC2 instance volumes and S3 objects for malware and known threats.
  name: Malware Protection
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Automatically send GuardDuty findings to Security Hub for centralized security management.
  name: AWS Security Hub
- description: Trigger automated responses to findings using EventBridge rules and Lambda functions.
  name: Amazon EventBridge
- description: Enable GuardDuty organization-wide for centralized multi-account threat monitoring.
  name: AWS Organizations
- description: Investigate GuardDuty findings in depth using Detective for root cause analysis.
  name: Amazon Detective
- description: Combine with Macie for comprehensive data security and threat detection.
  name: Amazon Macie
jsonld:
- class_count: 247
  name: Amazon Guardduty Context
  property_count: 297
  slug: amazon-guardduty-context
layout: provider
modified: '2026-04-19'
name: Amazon GuardDuty
rules:
- name: Amazon GuardDuty API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 2
  slug: amazon-guardduty-spectral-rules
skills: []
slug: amazon-guardduty
solutions: []
tags:
- Anomaly Detection
- AWS
- Compliance
- Machine Learning
- Monitoring
- Security
- Threat Detection
url: https://raw.githubusercontent.com/api-evangelist/amazon-guardduty/refs/heads/main/apis.yml
use_cases:
- description: Detect compromised AWS credentials and unauthorized API calls using ML-based anomaly detection.
  name: Account Compromise Detection
- description: Identify suspicious behavior from privileged users or compromised internal accounts.
  name: Insider Threat Monitoring
- description: Detect and alert on unauthorized cryptocurrency mining using EC2 or Lambda resources.
  name: Cryptocurrency Mining Detection
- description: Scan workloads and data for malware and ransomware threats.
  name: Malware Detection
- description: Identify unusual data access patterns and potential exfiltration from S3 buckets.
  name: Data Exfiltration Prevention
---
