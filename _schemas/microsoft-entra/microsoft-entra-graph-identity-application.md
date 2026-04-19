---
description: Represents an application registration in Microsoft Entra ID. Defines the app's identity configuration, credentials, permissions requested, and reply URLs.
layout: schema
name: Application
properties_list:
- description: Unique identifier for the application object (GUID). This is the object ID, not the appId.
  name: id
  type: string
- description: The unique application identifier assigned by Microsoft Entra ID (also known as the client ID)
  name: appId
  type: string
- description: The display name for the application
  name: displayName
  type: string
- description: An optional description of the application
  name: description
  type: '[''string'', ''null'']'
- description: Specifies which Microsoft accounts are supported for the application
  name: signInAudience
  type: string
- description: URIs that uniquely identify the application within its Azure AD tenant or verified custom domain
  name: identifierUris
  type: array
- description: Specifies the resources that the application needs access to and the set of OAuth permission scopes and app roles needed under each resource
  name: requiredResourceAccess
  type: array
- description: Collection of roles defined for the application that can be assigned to users, groups, or service principals
  name: appRoles
  type: array
- description: Collection of certificate credentials associated with the app
  name: keyCredentials
  type: array
- description: Collection of password credentials (client secrets)
  name: passwordCredentials
  type: array
- description: Public client settings for mobile and desktop apps
  name: publicClient
  type: object
- description: Custom strings used to categorize and identify the application
  name: tags
  type: array
- description: The date and time the application was registered
  name: createdDateTime
  type: string
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-graph-identity-application-schema.json
slug: microsoft-entra-graph-identity-application
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
title: Application
---
