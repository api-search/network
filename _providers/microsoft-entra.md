---
api_count: 14
apis:
- description: Core identity and access management API for user authentication, authorization, and directory management.
  name: Microsoft Entra ID (Azure AD) API
  slug: graph-identity
- description: API for identity risk detection, investigation, and remediation.
  name: Microsoft Entra ID Protection API
  slug: id-protection
- description: API for managing conditional access policies and controls.
  name: Microsoft Entra Conditional Access API
  slug: conditional-access
- description: API for managing privileged access and just-in-time administration.
  name: Microsoft Entra Privileged Identity Management API
  slug: pim
- description: API for issuing and verifying decentralized identity credentials.
  name: Microsoft Entra Verified ID API
  slug: verified-id
- description: API for managing customer and partner identity and access management.
  name: Microsoft Entra External ID API
  slug: external-id
- description: API for managing identity governance including access reviews, entitlement management, and lifecycle workflows to ensure the right people have the right access at the right time.
  name: Microsoft Entra ID Governance API
  slug: id-governance
- description: API for registering, configuring, and managing applications and service principals in Microsoft Entra ID.
  name: Microsoft Entra Application Management API
  slug: application-management
- description: API for managing user authentication methods including FIDO2 security keys, passwordless phone sign-in, Microsoft Authenticator, and MFA registration.
  name: Microsoft Entra Authentication Methods API
  slug: authentication-methods
- description: API for managing and securing identities for software workloads such as applications, services, scripts, and containers.
  name: Microsoft Entra Workload ID API
  slug: workload-id
- description: API for automating user provisioning and deprovisioning using SCIM protocol, including API-driven inbound provisioning from any system of record.
  name: Microsoft Entra Provisioning API
  slug: provisioning
- description: API for managing Microsoft Entra Internet Access and Microsoft Entra Private Access, providing identity-centric secure web gateway and zero-trust network access.
  name: Microsoft Entra Global Secure Access API
  slug: global-secure-access
- description: API endpoints for OAuth 2.0, OpenID Connect, and SAML authentication protocols enabling application integration with Microsoft Entra ID.
  name: Microsoft Identity Platform API
  slug: identity-platform
- description: API for creating, securing, and monitoring AI agent identities, providing authentication, authorization, and lifecycle management for AI agents.
  name: Microsoft Entra Agent ID API
  slug: agent-id
capabilities:
- description: Unified workflow for managing identity and access including users, groups, applications, and service principals in Microsoft Entra ID. Used by IT administrators and identity engineers.
  name: Microsoft Entra Identity and Access Management
  slug: identity-and-access
common:
- title: ''
  type: Portal
  url: https://entra.microsoft.com/
- title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/entra/fundamentals/
- title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/microsoft-entra-azure-ad-blog/bg-p/Identity
- title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/entra/fundamentals/how-to-get-support
- title: ''
  type: StatusPage
  url: https://status.azure.com/
- title: ''
  type: TermsOfService
  url: https://www.microsoft.com/licensing/terms/
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new
- title: ''
  type: SDK
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing
- title: ''
  type: JSONLD
  url: json-ld/microsoft-entra-context.jsonld
- title: ''
  type: JSONSchema
  url: json-schema/microsoft-entra-user-schema.json
- title: ''
  type: JSONSchema
  url: json-schema/microsoft-entra-application-schema.json
- title: Graph Identity API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/graph-identity.yaml
- title: Identity and Access Management Workflow
  type: NaftikoCapability
  url: capabilities/identity-and-access.yaml
created: '2024-01-01'
description: Microsoft Entra (formerly Azure Active Directory) provides identity and access management services including authentication, authorization, and directory services.
features:
- description: Manage user identities, authentication, and authorization across cloud and hybrid environments with single sign-on.
  name: Identity and Access Management
- description: Enforce adaptive access policies based on user, device, location, and risk signals for zero trust security.
  name: Conditional Access
- description: Automate access reviews, entitlement management, and lifecycle workflows to ensure proper access controls.
  name: Identity Governance
- description: Manage, control, and monitor privileged access with just-in-time and approval-based activation.
  name: Privileged Identity Management
- description: Issue and verify decentralized identity credentials using open standards for portable, self-sovereign identity.
  name: Verified ID
- description: Enable secure collaboration with external partners and customers through B2B and B2C identity management.
  name: External Identities
- description: Provide identity-centric secure web gateway and zero-trust network access for internet and private resources.
  name: Global Secure Access
- description: Secure and manage identities for applications, services, scripts, and containers running as software workloads.
  name: Workload Identities
image: https://www.microsoft.com/en-us/security/content/dam/microsoft/final/security/includes/microsoft-entra-logo.svg
integrations:
- description: Deep integration for identity and access management across all Microsoft 365 applications and services.
  name: Microsoft 365
- description: Native identity provider for Azure resources including VMs, databases, storage, and managed identities.
  name: Azure Services
- description: Hybrid identity synchronization with on-premises Active Directory using Azure AD Connect.
  name: Active Directory
- description: SAML and SCIM integration for single sign-on and automated user provisioning with Salesforce.
  name: Salesforce
- description: SSO and automated provisioning integration with ServiceNow ITSM platform.
  name: ServiceNow
- description: Inbound provisioning from Workday HR to automate user lifecycle management.
  name: Workday
- description: SSO and provisioning integration with SAP applications and S/4HANA.
  name: SAP
- description: Cross-platform identity federation and migration support with Okta identity provider.
  name: Okta
jsonld:
- class_count: 0
  name: Microsoft Entra Context
  property_count: 5
  slug: microsoft-entra-context
- class_count: 0
  name: Microsoft Entra Graph Identity Context
  property_count: 0
  slug: microsoft-entra-graph-identity-context
layout: provider
modified: '2026-04-18'
name: Microsoft Entra
rules:
- name: Microsoft Entra API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: microsoft-entra-spectral-rules
skills: []
slug: microsoft-entra
solutions: []
tags:
- Access Management
- Authentication
- Azure AD
- Entra
- Identity
- Identity Governance
- Microsoft
- Network Security
- Security
- Zero Trust
url: https://raw.githubusercontent.com/api-evangelist/microsoft-entra/refs/heads/main/apis.yml
use_cases:
- description: Implement zero trust architecture with identity-based access controls, conditional access policies, and continuous verification.
  name: Zero Trust Implementation
- description: Synchronize and manage identities across on-premises Active Directory and cloud environments.
  name: Hybrid Identity Management
- description: Enable SSO for thousands of SaaS and on-premises applications with SAML, OIDC, and password-based authentication.
  name: Application Single Sign-On
- description: Automate user lifecycle management with SCIM-based provisioning and deprovisioning across integrated applications.
  name: Automated User Provisioning
- description: Create, secure, and monitor identities for AI agents with authentication, authorization, and lifecycle management.
  name: AI Agent Identity Management
---
