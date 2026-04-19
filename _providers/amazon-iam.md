---
api_count: 1
apis:
- description: The AWS IAM API provides programmatic access to manage users, groups, roles, policies, and access keys for securing access to AWS services and resources.
  name: AWS IAM API
  slug: aws-iam-api
capabilities:
- description: Unified capability for cloud administrators to manage IAM users, roles, groups, and policies for AWS account access control and security governance.
  name: Amazon IAM - Access Management
  slug: iam-access-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/iam/
- title: ''
  type: Website
  url: https://aws.amazon.com/iam/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/IAM/latest/UserGuide/
- title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- title: ''
  type: Support
  url: https://aws.amazon.com/support/
- title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/iam/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-iam
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: JSONLD
  url: json-ld/amazon-iam-context.jsonld
- title: ''
  type: SpectralRules
  url: rules/amazon-iam-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/iam.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/iam-access-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-iam-vocabulary.yaml
created: '2026-03-16'
description: Amazon Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users, groups, roles, and policies, and use permissions to allow and deny their access to AWS resources. IAM is a feature of your AWS account offered at no additional charge.
features:
- description: Create, manage, and delete IAM users with fine-grained permissions.
  name: User Management
- description: Define IAM roles that can be assumed by users, services, or applications.
  name: Role-Based Access Control
- description: Create and attach identity-based and resource-based policies to control access.
  name: Policy Management
- description: Enable MFA for IAM users to add an extra layer of security.
  name: Multi-Factor Authentication
- description: Programmatically manage AWS access keys for long-term credentials.
  name: Access Key Management
- description: Use permission boundaries to define the maximum permissions an entity can have.
  name: Permission Boundaries
- description: Centrally control the maximum available permissions across AWS accounts.
  name: Service Control Policies
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Apply Service Control Policies across multiple AWS accounts in an organization.
  name: AWS Organizations
- description: Log all IAM API calls for auditing and compliance tracking.
  name: AWS CloudTrail
- description: Monitor IAM configuration changes and evaluate compliance with rules.
  name: AWS Config
- description: Centralize IAM security findings with other AWS security services.
  name: AWS Security Hub
- description: Federate Cognito user pool identities with IAM roles for application access.
  name: Amazon Cognito
jsonld:
- class_count: 0
  name: Amazon Iam Context
  property_count: 6
  slug: amazon-iam-context
layout: provider
modified: '2026-04-19'
name: Amazon IAM
rules:
- name: Amazon IAM API Rules
  rule_count: 20
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 8
  slug: amazon-iam-spectral-rules
skills: []
slug: amazon-iam
solutions: []
tags:
- Access Management
- Authentication
- Authorization
- AWS
- Identity
- Security
url: https://raw.githubusercontent.com/api-evangelist/amazon-iam/refs/heads/main/apis.yml
use_cases:
- description: Grant only the permissions required for specific tasks to reduce the attack surface.
  name: Least Privilege Access
- description: Enable users in one AWS account to assume roles in another account.
  name: Cross-Account Access
- description: Allow AWS services to access other services on your behalf through service roles.
  name: Service-to-Service Authorization
- description: Use STS to issue temporary security credentials for short-lived access.
  name: Temporary Credentials
- description: Audit IAM configurations to ensure compliance with security policies and regulations.
  name: Security Compliance
---
