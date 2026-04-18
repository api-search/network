---
description: Represents an app role assigned to a user, group, or service principal.
layout: schema
name: AppRoleAssignment
properties_list:
- description: ''
  name: id
  type: string
- description: The identifier of the app role. Set to the default app role ID of 00000000-0000-0000-0000-000000000000 if not specified.
  name: appRoleId
  type: string
- description: ''
  name: createdDateTime
  type: string
- description: The display name of the principal (user, group, or service principal).
  name: principalDisplayName
  type: string
- description: The unique identifier of the principal being granted the role.
  name: principalId
  type: string
- description: The type of the assigned principal (User, Group, or ServicePrincipal).
  name: principalType
  type: string
- description: The display name of the resource application.
  name: resourceDisplayName
  type: string
- description: The unique identifier of the resource service principal.
  name: resourceId
  type: string
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-app-role-assignment-schema.json
slug: microsoft-graph-identity-app-role-assignment
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
title: AppRoleAssignment
---
