---
description: Represents an application registration in Azure AD. An application object is the global definition of an application, specifying how tokens are issued, the resources the application needs to access, and the actions it can perform.
layout: schema
name: Application
properties_list:
- description: The unique identifier assigned by Azure AD when the app is registered. Also known as the client ID.
  name: appId
  type: string
- description: The display name for the application.
  name: displayName
  type: string
- description: A free text field to describe the application.
  name: description
  type: '[''string'', ''null'']'
- description: The date and time the application was registered.
  name: createdDateTime
  type: string
- description: URIs that identify the application within its Azure AD tenant. Also known as App ID URIs.
  name: identifierUris
  type: array
- description: The collection of key credentials (certificates) associated with the application.
  name: keyCredentials
  type: array
- description: The collection of password credentials (client secrets) associated with the application.
  name: passwordCredentials
  type: array
- description: The collection of roles defined for the application.
  name: appRoles
  type: array
- description: Specifies the resources that the application needs access to.
  name: requiredResourceAccess
  type: array
- description: Specifies the Microsoft accounts supported for the current application.
  name: signInAudience
  type: string
- description: Custom strings that can be used to categorize the application.
  name: tags
  type: array
- description: The verified publisher domain for the application.
  name: publisherDomain
  type: string
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-application-schema.json
slug: microsoft-graph-identity-application
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
title: Application
---
