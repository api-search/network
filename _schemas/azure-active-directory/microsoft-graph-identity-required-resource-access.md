---
description: Specifies the set of OAuth 2.0 permission scopes and app roles that an application requires access to.
layout: schema
name: RequiredResourceAccess
properties_list:
- description: The unique identifier for the resource that the application requires access to (e.g., Microsoft Graph).
  name: resourceAppId
  type: string
- description: ''
  name: resourceAccess
  type: array
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-required-resource-access-schema.json
slug: microsoft-graph-identity-required-resource-access
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
title: RequiredResourceAccess
---
