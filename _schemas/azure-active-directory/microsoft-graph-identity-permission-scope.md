---
description: Represents a delegated permission (OAuth2 scope).
layout: schema
name: PermissionScope
properties_list:
- description: ''
  name: adminConsentDescription
  type: string
- description: ''
  name: adminConsentDisplayName
  type: string
- description: ''
  name: id
  type: string
- description: ''
  name: isEnabled
  type: boolean
- description: ''
  name: type
  type: string
- description: ''
  name: userConsentDescription
  type: string
- description: ''
  name: userConsentDisplayName
  type: string
- description: The value to include in the scp claim in access tokens.
  name: value
  type: string
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-permission-scope-schema.json
slug: microsoft-graph-identity-permission-scope
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
title: PermissionScope
---
