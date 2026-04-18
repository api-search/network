---
description: Represents an application role that can be assigned to users, groups, or service principals.
layout: schema
name: AppRole
properties_list:
- description: Specifies whether this app role can be assigned to users and groups or to applications.
  name: allowedMemberTypes
  type: array
- description: ''
  name: description
  type: string
- description: ''
  name: displayName
  type: string
- description: ''
  name: id
  type: string
- description: ''
  name: isEnabled
  type: boolean
- description: The value to include in the roles claim in access tokens.
  name: value
  type: string
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-app-role-schema.json
slug: microsoft-graph-identity-app-role
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
title: AppRole
---
