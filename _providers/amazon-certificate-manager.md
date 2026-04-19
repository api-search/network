---
api_count: 1
apis:
- description: API for provisioning, managing, and deploying public and private SSL/TLS certificates for use with AWS services and your internal connected resources. Supports requesting certificates, describing cert
  name: Amazon Certificate Manager API
  slug: ''
capabilities:
- description: Unified workflow for managing SSL/TLS certificate lifecycles on AWS, enabling DevOps engineers and security teams to provision, inspect, and retire certificates for websites and internal services.
  name: Amazon Certificate Manager Certificate Lifecycle Management
  slug: certificate-lifecycle-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/certificate-manager/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/acm/
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
  url: https://console.aws.amazon.com/acm/
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
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/aws-certificate-manager
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: Security
  url: https://docs.aws.amazon.com/acm/latest/userguide/security.html
- title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- title: ''
  type: SpectralRules
  url: rules/amazon-certificate-manager-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-certificate-manager-vocabulary.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/certificate-lifecycle-management.yaml
created: '2024-01-15'
description: AWS Certificate Manager (ACM) handles the complexity of creating, storing, and renewing public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications, enabling you to manage certificate lifecycles centrally.
features:
- description: Managed renewal for Amazon-issued SSL/TLS certificates, reducing manual maintenance overhead.
  name: Automated Certificate Renewal
- description: Provision both public certificates validated via DNS or email, and private certificates issued by a private CA.
  name: Public and Private Certificates
- description: Strong encryption and key management best practices for protecting and storing private keys.
  name: FIPS-Compliant Key Storage
- description: Deploy certificates to CloudFront, Elastic Load Balancing, API Gateway, and other integrated AWS services at no cost.
  name: Integrated AWS Service Deployment
- description: Provision and manage certificates for EC2, containers, on-premises hosts, and multicloud workloads.
  name: Hybrid and Multicloud Support
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Deploy ACM certificates to CloudFront distributions for HTTPS content delivery.
  name: Amazon CloudFront
- description: Attach ACM certificates to Application, Network, and Classic Load Balancers.
  name: Elastic Load Balancing
- description: Use ACM certificates for custom domain names in API Gateway.
  name: Amazon API Gateway
- description: Control access to ACM operations via IAM policies and roles.
  name: AWS IAM
- description: Audit all ACM API calls via CloudTrail for compliance and security monitoring.
  name: AWS CloudTrail
jsonld:
- class_count: 4
  name: Amazon Certificate Manager Context
  property_count: 8
  slug: amazon-certificate-manager-context
layout: provider
modified: '2026-04-19'
name: Amazon Certificate Manager
rules:
- name: Amazon Certificate Manager API Rules
  rule_count: 29
  severity_counts:
    error: 15
    hint: 0
    info: 3
    warn: 11
  slug: amazon-certificate-manager-spectral-rules
skills: []
slug: amazon-certificate-manager
solutions: []
tags:
- AWS
- Certificates
- Encryption
- Security
- SSL
- TLS
url: https://raw.githubusercontent.com/api-evangelist/amazon-certificate-manager/refs/heads/main/apis.yml
use_cases:
- description: Securely terminate HTTPS traffic to public websites and web applications using ACM certificates.
  name: Website Protection
- description: Protect private network communication between servers, mobile devices, IoT devices, and internal applications.
  name: Internal Service Security
- description: Automated certificate lifecycle management prevents certificate expiration-related service downtime.
  name: Uptime Maintenance
- description: Centralize certificate management to meet compliance requirements and simplify security audits.
  name: Compliance and Audit
---
