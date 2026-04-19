---
api_count: 1
apis:
- description: The AWS Firewall Manager API provides programmatic access to create and manage security policies, compliance status, and protection configurations for AWS WAF, Shield, and VPC security groups across y
  name: AWS Firewall Manager API
  slug: aws-firewall-manager-api
capabilities:
- description: Centrally manage WAF, Shield, Network Firewall, and security group policies across AWS accounts.
  name: Amazon Firewall Manager Security Governance
  slug: amazon-firewall-manager-security-governance
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/firewall-manager/
- title: ''
  type: Website
  url: https://aws.amazon.com/firewall-manager/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html
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
  url: https://aws.amazon.com/blogs/security/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/wafv2/fmsv2/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-firewall-manager
- title: ''
  type: SpectralRules
  url: rules/amazon-firewall-manager-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/firewall-manager.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/amazon-firewall-manager-security-governance.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-firewall-manager-vocabulary.yaml
- title: ''
  type: JSON-LD
  url: json-ld/amazon-firewall-manager-context.jsonld
created: '2026-03-16'
description: AWS Firewall Manager is a security management service that allows you to centrally configure and manage firewall rules across your accounts and applications in AWS Organizations. It makes it easier to bring new applications and resources into compliance with security policies.
features:
- description: Define and enforce WAF, Shield Advanced, Network Firewall, and security group policies from a single pane of glass across all AWS accounts.
  name: Centralized Policy Management
- description: Automatically remediate non-compliant resources so that new accounts and resources are always protected.
  name: Automatic Remediation
- description: Manage security policies across hundreds of AWS accounts within an AWS Organization.
  name: Multi-Account Support
- description: View policy compliance status per account and resource with detailed violation reports.
  name: Compliance Visibility
- description: Group AWS resources by type for targeted policy application and management.
  name: Resource Sets
- description: Apply policies to resources based on AWS resource tags for fine-grained scope control.
  name: Tag-Based Targeting
- description: Deploy and manage third-party firewall appliances through AWS Marketplace with Firewall Manager.
  name: Third-Party Firewall Support
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Manage Firewall Manager policies across all accounts in the organization hierarchy.
  name: AWS Organizations
- description: Centrally create and deploy WAF rule groups and web ACLs across accounts.
  name: AWS WAF
- description: Enable and manage Shield Advanced protection for all DDoS-sensitive resources.
  name: AWS Shield Advanced
- description: Deploy centrally managed network firewall policies across VPCs.
  name: AWS Network Firewall
- description: Manage DNS Firewall rule groups for Route 53 Resolver across accounts.
  name: Amazon Route 53 Resolver
- description: Monitor compliance metrics and set alarms for non-compliant resources.
  name: Amazon CloudWatch
- description: Send Firewall Manager compliance findings to Security Hub for centralized security posture management.
  name: AWS Security Hub
- description: Control who can create, modify, and view Firewall Manager policies using IAM permissions.
  name: AWS IAM
jsonld:
- class_count: 5
  name: Amazon Firewall Manager Context
  property_count: 14
  slug: amazon-firewall-manager-context
layout: provider
modified: '2026-04-19'
name: Amazon Firewall Manager
rules:
- name: Amazon Firewall Manager API Rules
  rule_count: 25
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 14
  slug: amazon-firewall-manager-spectral-rules
skills: []
slug: amazon-firewall-manager
solutions: []
tags:
- AWS
- Compliance
- Firewall
- Network Security
- Security
url: https://raw.githubusercontent.com/api-evangelist/amazon-firewall-manager/refs/heads/main/apis.yml
use_cases:
- description: Enforce standard WAF rule sets across all CloudFront distributions and ALBs organization-wide.
  name: WAF Rule Standardization
- description: Mandate Shield Advanced protection for all internet-facing resources across accounts.
  name: DDoS Protection Baseline
- description: Audit and remediate overly permissive security group rules across EC2 and VPC resources.
  name: Security Group Governance
- description: Deploy and manage AWS Network Firewall across VPCs in multiple accounts from a central policy.
  name: Network Firewall Deployment
- description: Monitor and report on firewall policy compliance for SOC 2, PCI DSS, and regulatory requirements.
  name: Compliance Reporting
- description: Automatically apply security policies to new AWS accounts as they join the organization.
  name: New Account Onboarding
---
