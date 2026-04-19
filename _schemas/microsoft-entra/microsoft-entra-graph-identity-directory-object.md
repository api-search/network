---
description: Base type for many directory resources including users, groups, and service principals
layout: schema
name: DirectoryObject
properties_list:
- description: The OData type string for the directory object
  name: '@odata.type'
  type: string
- description: Unique identifier for the directory object
  name: id
  type: string
- description: The display name of the directory object
  name: displayName
  type: '[''string'', ''null'']'
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-graph-identity-directory-object-schema.json
slug: microsoft-entra-graph-identity-directory-object
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
title: DirectoryObject
---
