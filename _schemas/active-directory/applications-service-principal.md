---
description: A Microsoft Entra service principal — the local tenant instance of an application
layout: schema
name: ServicePrincipal
properties_list:
- description: Unique identifier for the service principal object
  name: id
  type: string
- description: Application (client) ID of the associated application registration
  name: appId
  type: string
- description: Display name for the service principal
  name: displayName
  type: string
- description: Type of service principal
  name: servicePrincipalType
  type: string
- description: True if the service principal account is enabled
  name: accountEnabled
  type:
  - boolean
  - 'null'
- description: Application roles exposed by the associated application
  name: appRoles
  type: array
- description: Delegated permission scopes exposed by the application
  name: oauth2PermissionScopes
  type: array
- description: Home page or landing page of the application
  name: homepage
  type:
  - string
  - 'null'
- description: URL to direct users for sign-in (for SP-initiated SAML SSO)
  name: loginUrl
  type:
  - string
  - 'null'
- description: URLs where tokens are sent after authentication
  name: replyUrls
  type: array
- description: Strings that categorize the application
  name: tags
  type: array
- description: ''
  name: createdDateTime
  type:
  - string
  - 'null'
provider_name: Microsoft Active Directory
provider_slug: active-directory
schema_file: json-schema/applications-service-principal-schema.json
slug: applications-service-principal
tags:
- Active Directory
- Authentication
- Authorization
- Directory Services
- Identity Management
- Microsoft Entra
- Zero Trust
title: ServicePrincipal
---
