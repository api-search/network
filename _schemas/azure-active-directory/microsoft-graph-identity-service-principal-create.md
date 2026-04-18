---
description: Properties required when creating a new service principal.
layout: schema
name: ServicePrincipalCreate
properties_list:
- description: The appId of the application to create a service principal for.
  name: appId
  type: string
- description: ''
  name: displayName
  type: string
- description: ''
  name: accountEnabled
  type: boolean
- description: ''
  name: appRoleAssignmentRequired
  type: boolean
- description: ''
  name: tags
  type: array
- description: ''
  name: notificationEmailAddresses
  type: array
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-service-principal-create-schema.json
slug: microsoft-graph-identity-service-principal-create
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
title: ServicePrincipalCreate
---
