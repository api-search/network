---
description: Represents an app role granted to a user, group, or service principal
layout: schema
name: AppRoleAssignment
properties_list:
- description: Unique identifier for the assignment (GUID)
  name: id
  type: string
- description: The ID of the app role to assign. Use the default role ID 00000000-0000-0000-0000-000000000000 for default access.
  name: appRoleId
  type: string
- description: The unique identifier of the user, group, or service principal being granted the app role
  name: principalId
  type: string
- description: The type of the assigned principal
  name: principalType
  type: string
- description: Display name of the principal
  name: principalDisplayName
  type: string
- description: The unique identifier of the resource service principal to which the assignment is made
  name: resourceId
  type: string
- description: Display name of the resource application
  name: resourceDisplayName
  type: string
- description: Time when the app role assignment was created
  name: createdDateTime
  type: string
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-graph-identity-app-role-assignment-schema.json
slug: microsoft-entra-graph-identity-app-role-assignment
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
title: AppRoleAssignment
---
