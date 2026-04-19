---
api_count: 1
apis:
- description: The Amazon Security Lake API provides programmatic access to create and manage data lakes, data sources, subscribers, and log sources for centralizing and analyzing security data across your organizat
  name: Amazon Security Lake API
  slug: ''
capabilities:
- description: Unified capability for managing a centralized security data lake including data lake configuration, log source ingestion, and subscriber access management. Used by Security Data Engineers and CISO tea
  name: Amazon Security Lake Security Data Lake
  slug: security-data-lake
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/security-lake/
- title: ''
  type: GettingStarted
  url: https://aws.amazon.com/security-lake/getting-started/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/security-lake/
- title: ''
  type: APIReference
  url: https://docs.aws.amazon.com/security-lake/latest/APIReference/
- title: ''
  type: Console
  url: https://console.aws.amazon.com/securitylake/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Pricing
  url: https://aws.amazon.com/security-lake/pricing/
- title: ''
  type: FAQ
  url: https://aws.amazon.com/security-lake/faqs/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/tag/amazon-security-lake/
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
  url: https://stackoverflow.com/questions/tagged/amazon-security-lake
- title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: SpectralRules
  url: rules/amazon-security-lake-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-security-lake-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/security-data-lake.yaml
- title: ''
  type: JSON-LD
  url: json-ld/amazon-security-lake-context.jsonld
- title: ''
  type: JSONStructure
  url: json-structure/amazon-security-lake-data-lake-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/amazon-security-lake-log-source-structure.json
- title: ''
  type: JSONStructure
  url: json-structure/amazon-security-lake-subscriber-structure.json
- title: ''
  type: Example
  url: examples/amazon-security-lake-data-lake-example.json
- title: ''
  type: Example
  url: examples/amazon-security-lake-log-source-example.json
- title: ''
  type: Example
  url: examples/amazon-security-lake-subscriber-example.json
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/amazon-security-lake.yaml
created: '2026-03-16'
description: Amazon Security Lake is a service that automatically centralizes an organization's security data from cloud, on-premises, and custom sources into a purpose-built data lake stored in your own Amazon S3. It manages the data lifecycle to help you optimize storage and supports OCSF (Open Cybersecurity Schema Framework) for normalized security data analysis.
features:
- description: Automatically centralizes security data from AWS services, third-party tools, and custom sources into a single data lake.
  name: Automatic Data Centralization
- description: Converts security data to the Open Cybersecurity Schema Framework (OCSF) for standardized analysis across tools.
  name: OCSF Normalization
- description: Stores all security data in Apache Parquet format optimized for analytical query performance.
  name: Apache Parquet Format
- description: Centralizes security data across an entire AWS Organization from all accounts and regions.
  name: Multi-Account Support
- description: Automatically manages storage lifecycle with configurable retention and tiering policies.
  name: Lifecycle Management
- description: Grant third-party SIEMs and analytics tools direct query access to your security data lake.
  name: Subscriber Access
- description: Native connectors for CloudTrail, VPC Flow Logs, Route 53, Security Hub, and EKS audit logs.
  name: Native AWS Integration
- description: Ingest custom and third-party security data sources in OCSF format.
  name: Custom Log Sources
image: ''
integrations:
- description: Native connector for management event and data event logs from CloudTrail.
  name: AWS CloudTrail
- description: Ingest VPC network flow logs for network traffic analysis.
  name: Amazon VPC Flow Logs
- description: Collect DNS query logs for domain analysis and threat detection.
  name: Amazon Route 53
- description: Aggregate Security Hub findings into the security data lake.
  name: AWS Security Hub
- description: Ingest Kubernetes audit logs from Amazon EKS clusters.
  name: Amazon EKS
- description: All security data is stored in S3 buckets within your own AWS account.
  name: Amazon S3
- description: Control fine-grained subscriber access using AWS Lake Formation permissions.
  name: AWS Lake Formation
- description: SIEM subscriber integration for Splunk to query Security Lake data directly.
  name: Splunk
- description: Connect Microsoft Sentinel as a subscriber to consume OCSF-normalized data.
  name: Microsoft Sentinel
- description: Ingest CrowdStrike endpoint detection findings as a custom log source.
  name: CrowdStrike
jsonld:
- class_count: 3
  name: Amazon Security Lake Context
  property_count: 18
  slug: amazon-security-lake-context
layout: provider
modified: '2026-04-19'
name: Amazon Security Lake
rules:
- name: Amazon Security Lake API Rules
  rule_count: 21
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 10
  slug: amazon-security-lake-spectral-rules
skills: []
slug: amazon-security-lake
solutions: []
tags:
- AWS
- Data Lake
- Security
- SIEM
- Threat Detection
url: https://aws.amazon.com/security-lake/
use_cases:
- description: Aggregate all security data from across a multi-account AWS environment into one queryable data lake.
  name: Security Data Centralization
- description: Provide SIEM platforms like Splunk, Sumo Logic, and Microsoft Sentinel direct access to normalized security data.
  name: SIEM Integration
- description: Enable security analysts to query normalized OCSF data for threat hunting and forensic investigation.
  name: Threat Hunting
- description: Retain security logs in a cost-optimized data lake for compliance audit requirements.
  name: Compliance Data Retention
- description: Run advanced analytics and ML models against normalized security data for anomaly detection.
  name: Security Analytics
- description: Centralize security data from on-premises and other cloud providers alongside AWS security data.
  name: Multi-Cloud Security Data
---
