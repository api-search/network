---
description: Defines an OAuth 2.0 delegated permission scope exposed by a web API application
layout: schema
name: PermissionScope
properties_list:
- description: Unique identifier for the scope
  name: id
  type: string
- description: The value that identifies the scope in OAuth 2.0 authorization requests
  name: value
  type: string
- description: Whether the scope can be consented to by a user or requires admin consent
  name: type
  type: string
- description: Display name shown on the admin consent experience
  name: adminConsentDisplayName
  type: string
- description: Description shown on the admin consent experience
  name: adminConsentDescription
  type: string
- description: Display name shown on the user consent experience
  name: userConsentDisplayName
  type: '[''string'', ''null'']'
- description: Description shown on the user consent experience
  name: userConsentDescription
  type: '[''string'', ''null'']'
- description: Whether the scope is enabled and can be requested
  name: isEnabled
  type: boolean
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-graph-identity-permission-scope-schema.json
slug: microsoft-entra-graph-identity-permission-scope
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
title: PermissionScope
---
