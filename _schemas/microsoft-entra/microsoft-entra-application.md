---
description: Schema for a Microsoft Entra ID application registration as represented in the Microsoft Graph API. Defines the application's identity configuration, credentials, permissions, redirect URIs, and sign-in settings.
layout: schema
name: Microsoft Entra Application
properties_list:
- description: Unique identifier for the application object (GUID). This is the directory object ID, not the appId/client ID.
  name: id
  type: string
- description: The unique application (client) identifier assigned by Microsoft Entra ID during app registration.
  name: appId
  type: string
- description: The display name for the application.
  name: displayName
  type: string
- description: Free text field to provide a description of the application object to end users.
  name: description
  type:
  - string
  - 'null'
- description: Specifies which Microsoft accounts are supported for the current application.
  name: signInAudience
  type: string
- description: User-defined URIs that uniquely identify a Web application within its Microsoft Entra tenant or verified custom domain (e.g., api://contoso.com/myapp).
  name: identifierUris
  type: array
- description: ''
  name: web
  type: object
- description: ''
  name: spa
  type: object
- description: ''
  name: publicClient
  type: object
- description: ''
  name: api
  type: object
- description: Specifies the resources that the application needs access to and the set of OAuth permission scopes and app roles required under each resource.
  name: requiredResourceAccess
  type: array
- description: Collection of roles defined for the application. These roles can be assigned to users, groups, or service principals.
  name: appRoles
  type: array
- description: Collection of key (certificate) credentials associated with the application for token signing and verification.
  name: keyCredentials
  type: array
- description: Collection of password credentials (client secrets) associated with the application.
  name: passwordCredentials
  type: array
- description: ''
  name: optionalClaims
  type: object
- description: ''
  name: info
  type: object
- description: Custom strings that can be used to categorize and identify the application.
  name: tags
  type: array
- description: Configures the groups claim issued in user or OAuth 2.0 access tokens.
  name: groupMembershipClaims
  type:
  - string
  - 'null'
- description: Specifies the fallback application type as public client (e.g., installed application on a mobile device). Default is false.
  name: isFallbackPublicClient
  type:
  - boolean
  - 'null'
- description: The default redirect URI. If specified, it is used when no specific redirect URI is matched.
  name: defaultRedirectUri
  type:
  - string
  - 'null'
- description: Publisher certification status of the application.
  name: certification
  type:
  - object
  - 'null'
- description: The verified publisher domain for the application.
  name: publisherDomain
  type: string
- description: The date and time the application was registered.
  name: createdDateTime
  type: string
- description: The date and time the application was deleted.
  name: deletedDateTime
  type:
  - string
  - 'null'
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-application-schema.json
slug: microsoft-entra-application
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
title: Microsoft Entra Application
---
