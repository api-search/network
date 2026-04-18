---
description: Properties required when creating a new application registration.
layout: schema
name: ApplicationCreate
properties_list:
- description: The display name for the application.
  name: displayName
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: signInAudience
  type: string
- description: ''
  name: identifierUris
  type: array
- description: ''
  name: appRoles
  type: array
- description: ''
  name: requiredResourceAccess
  type: array
- description: ''
  name: tags
  type: array
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-application-create-schema.json
slug: microsoft-graph-identity-application-create
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
title: ApplicationCreate
---
