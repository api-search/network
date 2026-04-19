---
api_count: 2
apis:
- description: Amazon Cognito User Pools API provides user directory management, sign-up, sign-in, and token-based authentication for web and mobile applications. It supports multi-factor authentication, account rec
  name: Cognito User Pools API
  slug: ''
- description: Amazon Cognito Identity Pools (Federated Identities) API enables developers to create unique identities for users and federate them with identity providers. It provides temporary, limited-privilege AW
  name: Cognito Identity Pools API
  slug: ''
capabilities:
- description: Workflow capability for managing user authentication, identity federation, and access control using Amazon Cognito User Pools and Identity Pools. Used by application developers and platform administra
  name: Amazon Cognito User Authentication
  slug: user-authentication
common:
- title: ''
  type: Portal
  url: https://aws.amazon.com/
- title: ''
  type: Website
  url: https://aws.amazon.com/cognito/
- title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cognito/
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
  url: https://console.aws.amazon.com/cognito/
- title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/billing/signup
- title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-cognito
- title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- title: ''
  type: SpectralRules
  url: rules/amazon-cognito-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/user-authentication.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/amazon-cognito-vocabulary.yaml
created: '2016-04-18'
description: Amazon Cognito is a fully managed user identity and authentication service that enables developers to add sign-up, sign-in, and access control to web and mobile applications. It supports OAuth 2.0, SAML 2.0, and OpenID Connect standards, providing secure user directories that scale to millions of users. Cognito offers user pools for authentication and identity pools for authorization, allowing integration with social identity providers and enterprise identity systems.
features:
- description: Fully managed user directories with sign-up, sign-in, and account management supporting millions of users.
  name: User Pools
- description: Grant temporary AWS credentials to authenticated users from social identity providers, SAML, or user pools.
  name: Identity Pools (Federated Identities)
- description: Add SMS-based, TOTP, or email-based MFA to user pools for enhanced security.
  name: Multi-Factor Authentication
- description: Standards-compliant OAuth 2.0 authorization server with OIDC support for easy integration.
  name: OAuth 2.0 and OpenID Connect
- description: Federate with Google, Facebook, Amazon, Apple, and any OIDC or SAML 2.0 compatible provider.
  name: Social Identity Providers
- description: Risk-based adaptive authentication, compromised credential detection, and IP-based restriction.
  name: Advanced Security Features
- description: Lambda triggers for custom authentication challenges, migration, pre/post sign-up, and token customization.
  name: Customizable Authentication Flows
- description: Organize users into groups with associated IAM roles for role-based access control.
  name: User Groups
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Authorize API requests using Cognito User Pool authorizers.
  name: AWS API Gateway
- description: Customize authentication with Lambda triggers for sign-up, sign-in, and token generation.
  name: AWS Lambda
- description: Map Cognito groups and roles to IAM permissions for granular access control.
  name: AWS IAM
- description: Secure GraphQL APIs with Cognito User Pool authorization.
  name: AWS AppSync
- description: Offload authentication to Cognito from Application Load Balancers.
  name: Amazon ALB
- description: Social identity provider federation for consumer applications.
  name: Google, Facebook, Apple
- description: Enterprise identity provider federation via SAML for corporate SSO.
  name: SAML 2.0 Providers
jsonld:
- class_count: 1
  name: Amazon Cognito Cognito Context
  property_count: 35
  slug: amazon-cognito-cognito-context
- class_count: 0
  name: Amazon Cognito Context
  property_count: 3
  slug: amazon-cognito-context
- class_count: 50
  name: Amazon Cognito Identity Pools Context
  property_count: 55
  slug: amazon-cognito-identity-pools-context
- class_count: 269
  name: Amazon Cognito User Pools Context
  property_count: 308
  slug: amazon-cognito-user-pools-context
layout: provider
modified: '2026-04-19'
name: Amazon Cognito
rules:
- name: Amazon Cognito API Rules
  rule_count: 24
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 11
  slug: amazon-cognito-spectral-rules
skills: []
slug: amazon-cognito
solutions: []
tags:
- Authentication
- AWS
- Identity
- OAuth
- User Management
url: https://raw.githubusercontent.com/api-evangelist/amazon-cognito/refs/heads/main/apis.yml
use_cases:
- description: Add user sign-up and sign-in to web and mobile applications without managing authentication infrastructure.
  name: Web and Mobile App Authentication
- description: Protect APIs using Cognito-issued JWT tokens validated by API Gateway or application code.
  name: API Authorization
- description: Federate with corporate SAML 2.0 identity providers for single sign-on in enterprise applications.
  name: Enterprise SSO
- description: Enable users to sign in with their Google, Facebook, or Apple credentials.
  name: Social Login
- description: Secure serverless applications with temporary AWS credentials dispensed through identity pools.
  name: Serverless App Security
- description: Create isolated user pools per tenant for multi-tenant SaaS applications.
  name: Multi-Tenant SaaS
---
