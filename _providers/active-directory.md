---
api_count: 10
apis:
- description: Manage the entire lifecycle of users in Microsoft Entra ID, including creating, reading, updating, and deleting user accounts, managing licenses, group memberships, authentication methods, and profile
  name: Microsoft Graph Users API
  slug: ''
- description: Create and manage Microsoft Entra security groups, Microsoft 365 groups, and distribution lists. Manage group memberships, owners, and settings. Groups enable efficient entitlement management for user
  name: Microsoft Graph Groups API
  slug: ''
- description: Register and manage Microsoft Entra applications and their associated service principals programmatically. Configure app permissions, OAuth2 permission grants, app role assignments, certificates, fede
  name: Microsoft Graph Applications and Service Principals API
  slug: ''
- description: Manage devices registered or joined to Microsoft Entra ID, including Entra joined, Entra registered, and hybrid Azure AD joined devices. Retrieve BitLocker recovery keys and Local Admin Password Solut
  name: Microsoft Graph Devices API
  slug: ''
- description: Manage Microsoft Entra built-in and custom directory roles, role assignments, and role-scoped administrative units. Assign administrator roles to users, groups, or service principals, and create scope
  name: Microsoft Graph Directory Roles and Administrative Units API
  slug: ''
- description: Create and manage Microsoft Entra Conditional Access policies that enforce access controls based on user, location, device, and risk signals. Configure named locations, authentication context class re
  name: Microsoft Graph Conditional Access API
  slug: ''
- description: Manage Microsoft Entra ID Governance features including access reviews, entitlement management (access packages, catalogs, and policies), Privileged Identity Management (PIM) for just-in-time role act
  name: Microsoft Graph Identity Governance API
  slug: ''
- description: Detect, investigate, and remediate identity-based risks using Microsoft Entra ID Protection. Access risk detections, risky users, risky service principals, and risk events, and feed data into SIEM too
  name: Microsoft Graph Identity Protection API
  slug: ''
- description: Manage authentication methods registered for users in Microsoft Entra ID, including FIDO2 security keys, Microsoft Authenticator, phone (SMS/voice call), email OTP, Windows Hello for Business, and tem
  name: Microsoft Graph Authentication Methods API
  slug: ''
- description: 'Access audit logs, sign-in logs, provisioning logs, and identity-related reports for monitoring, compliance, and troubleshooting. Stream logs to Azure Monitor and Log Analytics or to third-party SIEM '
  name: Microsoft Graph Identity and Access Reports API
  slug: ''
capabilities:
- description: Unified workflow for managing Microsoft Entra ID (Active Directory) identity and access operations including user lifecycle management, group management, and application registration. Used by IT admin
  name: Microsoft Active Directory Identity Management Operations
  slug: identity-management-operations
common:
- title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/graph
- title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/graph/get-started
- title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/overview
- title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/auth-concepts
- title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/graph/api/overview
- title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/graph/throttling
- title: ''
  type: SDK
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- title: ''
  type: CLI
  url: https://learn.microsoft.com/en-us/cli/azure/ad
- title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/
- title: ''
  type: StatusPage
  url: https://azure.status.microsoft.com/
- title: ''
  type: Support
  url: https://developer.microsoft.com/en-us/graph/support
- title: ''
  type: TermsOfService
  url: https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/privacystatement
- title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing
- title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/graph/changelog
- title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- title: ''
  type: GitHubRepository
  url: https://github.com/microsoftgraph/microsoft-graph-openapi
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/microsoft-graph
- title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/paths/m365-msgraph-associate/
- title: ''
  type: SpectralRules
  url: rules/active-directory-spectral-rules.yml
- title: ''
  type: NaftikoCapability
  url: capabilities/identity-management-operations.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/active-directory-vocabulary.yaml
- title: ''
  type: JSON-LD
  url: json-ld/active-directory-context.jsonld
created: '2024-01-01'
description: Microsoft Active Directory and Microsoft Entra ID provide identity and access management for organizations of all sizes. Microsoft Graph API is the unified REST API gateway for accessing and managing Microsoft Entra ID (formerly Azure Active Directory), including users, groups, applications, devices, conditional access policies, identity governance, and directory administration. Legacy on-premises Active Directory is managed through LDAP, Kerberos, and PowerShell protocols; cloud identity is managed through Microsoft Graph.
features:
- description: Single REST endpoint (graph.microsoft.com) for all Microsoft Entra identity and directory operations.
  name: Unified Identity API
- description: Full CRUD operations for user accounts including bulk operations, license assignment, and guest management.
  name: User Lifecycle Management
- description: Create and manage security groups, Microsoft 365 groups, and dynamic membership groups.
  name: Group Management
- description: Programmatic app registration, permission configuration, and service principal management.
  name: Application Registration
- description: Create, update, and evaluate Conditional Access policies via API for Zero Trust enforcement.
  name: Conditional Access Automation
- description: Just-in-time role activation, time-bound access, and PIM policy management via API.
  name: Privileged Identity Management
- description: Access risk signals, risky users, and risk detections for automated threat response.
  name: Identity Protection
- description: Manage MFA and passwordless authentication methods registered for users.
  name: Authentication Method Management
- description: Programmatic access to audit logs, sign-in logs, and provisioning logs for SIEM integration.
  name: Audit and Sign-in Logs
- description: Access reviews, entitlement management, and lifecycle workflows for automated IAM.
  name: Identity Governance
image: https://learn.microsoft.com/en-us/entra/media/index/active-directory.svg
integrations:
- description: Microsoft Entra ID (formerly Azure AD) is the cloud identity backbone accessed via Microsoft Graph.
  name: Azure Active Directory
- description: Microsoft Graph provides unified access to Microsoft 365 user data alongside identity operations.
  name: Microsoft 365
- description: Stream Microsoft Entra sign-in and audit logs to Azure Monitor Log Analytics for analysis.
  name: Azure Monitor
- description: Feed identity risk signals and audit logs into Microsoft Sentinel SIEM for threat hunting.
  name: Microsoft Sentinel
- description: Microsoft Graph Intune APIs integrate device management with identity policies.
  name: Intune
- description: Automate user provisioning to SaaS applications using Microsoft Entra SCIM provisioning.
  name: SCIM Providers
- description: Register and manage federated applications using SAML 2.0 and OpenID Connect via Microsoft Graph.
  name: SAML and OIDC Applications
jsonld:
- class_count: 1
  name: Active Directory Context
  property_count: 69
  slug: active-directory-context
layout: provider
modified: '2026-04-19'
name: Microsoft Active Directory
rules:
- name: Microsoft Active Directory API Rules
  rule_count: 33
  severity_counts:
    error: 14
    hint: 0
    info: 4
    warn: 15
  slug: active-directory-spectral-rules
skills: []
slug: active-directory
solutions: []
tags:
- Active Directory
- Authentication
- Authorization
- Directory Services
- Identity Management
- Microsoft Entra
- Zero Trust
url: ''
use_cases:
- description: Automate user account creation, attribute updates, and deprovisioning for HR-driven identity lifecycle.
  name: User Provisioning Automation
- description: Programmatically deploy and manage Conditional Access policies across the organization.
  name: Zero Trust Policy Enforcement
- description: Stream audit logs and sign-in events to security information and event management systems.
  name: SIEM Integration
- description: Automate app registration, permission grants, and app role assignments for developer self-service.
  name: Application Access Management
- description: Detect and respond to risky sign-ins and compromised accounts via Identity Protection APIs.
  name: Identity Risk Remediation
- description: Generate access reviews, entitlement reports, and audit logs for regulatory compliance.
  name: Compliance Reporting
- description: Enforce just-in-time privileged access and audit role assignments via PIM APIs.
  name: Privileged Access Governance
---
