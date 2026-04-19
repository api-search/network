---
description: Represents an instance of an application in a tenant. The service principal is the local representation used for sign-in and access to resources. It inherits certain properties from the application object.
layout: schema
name: ServicePrincipal
properties_list:
- description: Unique identifier for the service principal (GUID)
  name: id
  type: string
- description: The unique identifier for the associated application (application's appId). Required on create.
  name: appId
  type: string
- description: The display name for the service principal
  name: displayName
  type: string
- description: Description of the service principal's function
  name: description
  type: '[''string'', ''null'']'
- description: Identifies whether the service principal represents an application, a managed identity, or a legacy app
  name: servicePrincipalType
  type: string
- description: The display name exposed by the associated application
  name: appDisplayName
  type: string
- description: Contains the tenant ID where the application is registered
  name: appOwnerOrganizationId
  type: '[''string'', ''null'']'
- description: true if the service principal account is enabled; false otherwise
  name: accountEnabled
  type: boolean
- description: Home page or landing page of the application
  name: homepage
  type: '[''string'', ''null'']'
- description: URL where the service provider redirects the user to Microsoft Entra ID to authenticate (SAML sign-on)
  name: loginUrl
  type: '[''string'', ''null'']'
- description: URL used by Microsoft's authorization service to sign out a user
  name: logoutUrl
  type: '[''string'', ''null'']'
- description: URLs where user tokens are sent for sign-in or redirect URIs for authorization codes and access tokens
  name: replyUrls
  type: array
- description: Contains the list of identifierUris copied from the associated application plus the appId
  name: servicePrincipalNames
  type: array
- description: Custom strings used to categorize and identify the service principal. Values include WindowsAzureActiveDirectoryIntegratedApp.
  name: tags
  type: array
- description: The roles exposed by the application that this service principal represents
  name: appRoles
  type: array
- description: The delegated permission scopes exposed by the application
  name: oauth2PermissionScopes
  type: array
- description: If true, users and other service principals must first be granted an app role assignment before they can sign in or obtain tokens
  name: appRoleAssignmentRequired
  type: boolean
- description: Collection of certificate credentials
  name: keyCredentials
  type: array
- description: Collection of password credentials
  name: passwordCredentials
  type: array
- description: Date and time the service principal was created
  name: createdDateTime
  type: '[''string'', ''null'']'
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-graph-identity-service-principal-schema.json
slug: microsoft-entra-graph-identity-service-principal
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
title: ServicePrincipal
---
