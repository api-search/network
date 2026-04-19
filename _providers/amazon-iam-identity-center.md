---
api_count: 2
apis:
- description: Manages permission sets, account assignments, instances, and SSO configurations for centralized identity and access management across AWS accounts and organizations.
  name: AWS IAM Identity Center SSO Admin API
  slug: aws-sso-admin-api
- description: Manages users, groups, and group memberships in the IAM Identity Center identity store, enabling programmatic provisioning of workforce identities.
  name: AWS IAM Identity Center Identity Store API
  slug: aws-identitystore-api
capabilities:
- description: Unified capability for IT administrators to manage workforce identities, provision access to AWS accounts, and configure SSO for enterprise applications.
  name: Amazon IAM Identity Center - Identity and Access Management
  slug: identity-access-management
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/iam/identity-center/
- title: ''
  type: Website
  url: https://aws.amazon.com/iam/identity-center/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/singlesignon/
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
  url: https://aws.amazon.com/blogs/security/tag/aws-iam-identity-center/
- title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- title: ''
  type: Console
  url: https://console.aws.amazon.com/singlesignon/
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
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-iam-identity-center-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/sso-admin.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/shared/identitystore.yaml
- title: ''
  type: NaftikoCapability
  url: capabilities/identity-access-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-iam-identity-center-vocabulary.yaml
- title: ''
  type: JSONLD
  url: json-ld/amazon-iam-identity-center-context.jsonld
created: '2026-03-16'
description: AWS IAM Identity Center (successor to AWS Single Sign-On) is where you create, or connect, your workforce identities in AWS once and manage access centrally across your AWS organization. You can create user identities directly in IAM Identity Center, or bring them from Microsoft Active Directory, and then use IAM Identity Center to manage user access to AWS accounts and business applications with single sign-on.
features:
- description: Create and manage workforce user identities directly or connect from an external identity provider.
  name: Workforce Identity Management
- description: Enable employees to sign in once and access all assigned AWS accounts and business applications.
  name: Single Sign-On
- description: Manage access to multiple AWS accounts from a single place using permission sets.
  name: Centralized Access Management
- description: Connect Microsoft Active Directory, Okta, Azure AD, and other SAML 2.0 identity providers.
  name: External Identity Provider Integration
- description: Define and reuse permission policies that can be assigned to users across multiple AWS accounts.
  name: Permission Set Management
- description: Automatically provision and de-provision users and groups using SCIM 2.0.
  name: Automated Provisioning
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Sync users and groups from Active Directory for SSO and access management.
  name: Microsoft Active Directory
- description: Connect Okta as an external identity provider using SAML 2.0 and SCIM.
  name: Okta
- description: Federate with Azure AD for identity synchronization and SSO.
  name: Azure Active Directory
- description: Manage access across all accounts in an AWS Organization from a single SSO configuration.
  name: AWS Organizations
jsonld:
- class_count: 130
  name: Amazon Iam Identity Center Context
  property_count: 96
  slug: amazon-iam-identity-center-context
layout: provider
modified: '2026-04-19'
name: Amazon IAM Identity Center
rules:
- name: Amazon IAM Identity Center API Rules
  rule_count: 18
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 8
  slug: amazon-iam-identity-center-spectral-rules
skills: []
slug: amazon-iam-identity-center
solutions: []
tags:
- Access Control
- Authentication
- AWS
- Identity Management
- Single Sign-On
url: https://raw.githubusercontent.com/api-evangelist/amazon-iam-identity-center/refs/heads/main/apis.yml
use_cases:
- description: Enable employees to access all AWS accounts and business apps with a single set of credentials.
  name: Workforce SSO
- description: Manage access to dozens or hundreds of AWS accounts from a single control plane.
  name: Centralized AWS Account Access
- description: Grant temporary elevated access to AWS accounts without permanent permissions.
  name: Just-in-Time Access
- description: Centralize access logging and produce audit reports for security compliance reviews.
  name: Compliance and Audit
---
