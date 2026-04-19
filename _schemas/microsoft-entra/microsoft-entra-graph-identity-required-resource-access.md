---
description: Specifies the set of OAuth 2.0 permission scopes and app roles under a specified resource that an application requires access to
layout: schema
name: RequiredResourceAccess
properties_list:
- description: The unique identifier for the resource that the application requires access to (the appId of the target application)
  name: resourceAppId
  type: string
- description: The list of OAuth 2.0 permission scopes and app roles required from the specified resource
  name: resourceAccess
  type: array
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-graph-identity-required-resource-access-schema.json
slug: microsoft-entra-graph-identity-required-resource-access
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
title: RequiredResourceAccess
---
