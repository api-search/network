---
description: A Microsoft Entra application registration managed via Microsoft Graph
layout: schema
name: Application
properties_list:
- description: Unique identifier for the application object (not the client ID)
  name: id
  type: string
- description: The application (client) ID used in OAuth2 flows
  name: appId
  type: string
- description: Display name of the application
  name: displayName
  type: string
- description: Free text description for the application
  name: description
  type:
  - string
  - 'null'
- description: Microsoft account types supported by the application
  name: signInAudience
  type: string
- description: URIs that identify the application within the tenant
  name: identifierUris
  type: array
- description: Web platform configuration for the application
  name: web
  type: object
- description: API permissions required by the application
  name: requiredResourceAccess
  type: array
- description: Certificate credentials for the application
  name: keyCredentials
  type: array
- description: Client secret credential metadata (secret value only returned at creation)
  name: passwordCredentials
  type: array
- description: ''
  name: createdDateTime
  type:
  - string
  - 'null'
- description: ''
  name: deletedDateTime
  type:
  - string
  - 'null'
provider_name: Microsoft Active Directory
provider_slug: active-directory
schema_file: json-schema/applications-application-schema.json
slug: applications-application
tags:
- Active Directory
- Authentication
- Authorization
- Directory Services
- Identity Management
- Microsoft Entra
- Zero Trust
title: Application
---
