---
description: Represents a role defined by an application that can be assigned to users, groups, or service principals
layout: schema
name: AppRole
properties_list:
- description: Unique identifier for the app role
  name: id
  type: string
- description: Specifies whether the role can be assigned to users/groups, applications, or both
  name: allowedMemberTypes
  type: array
- description: Display name for the app role
  name: displayName
  type: string
- description: Description of the app role
  name: description
  type: '[''string'', ''null'']'
- description: Value that is included in the roles claim in authentication tokens
  name: value
  type: '[''string'', ''null'']'
- description: Whether the app role is enabled
  name: isEnabled
  type: boolean
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-graph-identity-app-role-schema.json
slug: microsoft-entra-graph-identity-app-role
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
title: AppRole
---
