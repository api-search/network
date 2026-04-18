---
description: Properties required when creating a new group.
layout: schema
name: GroupCreate
properties_list:
- description: The display name for the group.
  name: displayName
  type: string
- description: ''
  name: description
  type: string
- description: Set to ["Unified"] for Microsoft 365 groups. Omit for security groups.
  name: groupTypes
  type: array
- description: ''
  name: mailEnabled
  type: boolean
- description: ''
  name: mailNickname
  type: string
- description: ''
  name: securityEnabled
  type: boolean
- description: ''
  name: visibility
  type: string
- description: ''
  name: isAssignableToRole
  type: boolean
- description: 'List of directory object URLs to add as members. Example: https://graph.microsoft.com/v1.0/directoryObjects/{id}'
  name: members@odata.bind
  type: array
- description: List of directory object URLs to set as owners.
  name: owners@odata.bind
  type: array
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-group-create-schema.json
slug: microsoft-graph-identity-group-create
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
title: GroupCreate
---
