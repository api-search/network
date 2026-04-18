---
api_count: 10
apis:
- description: The Microsoft Graph API offers a single endpoint to access Azure AD data and other Microsoft 365 services.
  name: Microsoft Graph API
  slug: ''
- description: Microsoft Graph APIs for managing Microsoft Entra identity and network access capabilities, including user management, group management, application registration, conditional access policies, authenti
  name: Microsoft Graph Identity and Access API
  slug: ''
- description: Legacy API for accessing Azure AD (deprecated in favor of Microsoft Graph).
  name: Azure AD Graph API (Deprecated)
  slug: ''
- description: Authentication library for Azure AD (being replaced by MSAL).
  name: Azure AD Authentication Library (ADAL)
  slug: ''
- description: Modern authentication library for Microsoft identity platform.
  name: Microsoft Authentication Library (MSAL)
  slug: ''
- description: 'The Microsoft identity platform provides authentication and authorization services using standards-compliant implementations of OAuth 2.0 and OpenID Connect, enabling developers to build applications '
  name: Microsoft Identity Platform
  slug: ''
- description: Microsoft Entra Verified ID is a managed verifiable credentials service that enables organizations to issue, manage, and verify decentralized identity credentials based on W3C standards.
  name: Microsoft Entra Verified ID API
  slug: ''
- description: Microsoft Entra ID Governance APIs in Microsoft Graph enable automated access reviews, entitlement management, lifecycle workflows, and privileged identity management for identity governance scenarios
  name: Microsoft Entra ID Governance API
  slug: ''
- description: Microsoft Entra ID supports SCIM 2.0 protocol for automatic user and group provisioning to cloud applications, enabling automated identity lifecycle management through standardized REST APIs.
  name: Microsoft Entra SCIM Provisioning API
  slug: ''
- description: The Microsoft Entra PowerShell module provides cmdlets for managing Microsoft Entra resources programmatically, built on the Microsoft Graph PowerShell SDK.
  name: Microsoft Entra PowerShell
  slug: ''
capabilities:
- description: Unified identity and access management workflow combining user lifecycle, group management, application registration, and service principal operations. Used by IT administrators and identity engineers
  name: Azure AD Identity and Access Management
  slug: identity-and-access
common:
- title: ''
  type: Portal
  url: https://portal.azure.com/
- title: ''
  type: StatusPage
  url: https://status.azure.com/
- title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/azure-active-directory/bg-p/Azure-Active-Directory
- title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/active-directory/
- title: ''
  type: Training
  url: https://docs.microsoft.com/en-us/learn/azure/
- title: Entra Admin Center
  type: Portal
  url: https://entra.microsoft.com
- title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/graph
- title: Identity Developer Blog
  type: Blog
  url: https://devblogs.microsoft.com/identity/
- title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new
- title: Entra Documentation
  type: Documentation
  url: https://learn.microsoft.com/en-us/entra/identity/
- title: Graph Explorer
  type: Console
  url: https://developer.microsoft.com/en-us/graph/graph-explorer
- title: ''
  type: GitHubOrganization
  url: https://github.com/AzureAD
- title: ''
  type: OpenAPI
  url: openapi/microsoft-graph-identity-api.yml
- title: ''
  type: JSONSchema
  url: json-schema/azure-active-directory-user-schema.json
- title: ''
  type: JSONLD
  url: json-ld/azure-active-directory-context.jsonld
created: '2024-01-15'
description: Microsoft Azure Active Directory (Azure AD), now Microsoft Entra ID, is Microsoft's cloud-based identity and access management service, which helps employees sign in and access resources.
features:
- description: Enable users to sign in once and access all connected applications without re-authenticating.
  name: Single Sign-On
- description: Enforce granular access policies based on user, device, location, and risk signals for zero trust security.
  name: Conditional Access
- description: Add a second layer of security with phone, app, or hardware token verification for identity protection.
  name: Multi-Factor Authentication
- description: Automate user and group lifecycle management across cloud applications using SCIM 2.0 standard.
  name: SCIM User Provisioning
- description: Issue and verify decentralized identity credentials based on W3C standards for privacy-preserving identity verification.
  name: Verifiable Credentials
- description: Automate access reviews, entitlement management, and lifecycle workflows for identity governance at scale.
  name: Identity Governance
- description: Publish on-premises web applications externally with secure remote access without VPN infrastructure.
  name: Application Proxy
image: https://docs.microsoft.com/azure/media/index/active-directory.svg
integrations:
- description: Native identity provider for all Microsoft 365 applications including Teams, Outlook, SharePoint, and OneDrive.
  name: Microsoft 365
- description: Single sign-on and automated user provisioning for Salesforce CRM using SAML and SCIM protocols.
  name: Salesforce
- description: Federated authentication and automated user lifecycle management for ServiceNow ITSM platform.
  name: ServiceNow
- description: Cross-cloud identity federation enabling Azure AD users to access AWS resources with single sign-on.
  name: AWS
- description: HR-driven identity provisioning with automated user creation and attribute synchronization from Workday.
  name: Workday
jsonld:
- class_count: 1
  name: Azure Active Directory Context
  property_count: 6
  slug: azure-active-directory-context
- class_count: 0
  name: Microsoft Graph Identity Context
  property_count: 0
  slug: microsoft-graph-identity-context
layout: provider
modified: '2026-04-18'
name: Azure Active Directory
rules:
- name: Azure Active Directory API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: azure-active-directory-spectral-rules
skills: []
slug: azure-active-directory
solutions: []
tags:
- Authentication
- Authorization
- Identity
- Microsoft
- Microsoft Entra
- OAuth
- OpenID Connect
- SAML
- SCIM
- Single Sign-On
- Zero Trust
url: https://azure.microsoft.com/en-us/services/active-directory/
use_cases:
- description: Implement single sign-on across SaaS and on-premises applications for seamless employee access management.
  name: Enterprise SSO
- description: Enable secure collaboration with external partners and guests using Azure AD B2B identity federation.
  name: B2B Collaboration
- description: Build customer-facing applications with self-service sign-up, social identity providers, and branded login experiences.
  name: Customer Identity
- description: Implement zero trust architecture with conditional access policies, continuous access evaluation, and risk-based authentication.
  name: Zero Trust Security
- description: Automate user account creation, updates, and deprovisioning across connected SaaS applications using SCIM.
  name: Automated User Provisioning
---
