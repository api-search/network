---
description: Configuration for an application that exposes a web API.
layout: schema
name: ApiApplication
properties_list:
- description: If true, allows an application to use claims mapping without specifying a custom signing key.
  name: acceptMappedClaims
  type: '[''boolean'', ''null'']'
- description: Used for bundling consent. Lists client app IDs that are considered known clients of this API.
  name: knownClientApplications
  type: array
- description: The definition of the delegated permissions exposed by the web API.
  name: oauth2PermissionScopes
  type: array
- description: Lists applications that are pre-authorized with specified delegated permissions.
  name: preAuthorizedApplications
  type: array
- description: The access token version expected by this resource. Possible values are 1 or 2.
  name: requestedAccessTokenVersion
  type: '[''integer'', ''null'']'
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-api-application-schema.json
slug: microsoft-graph-identity-api-application
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
title: ApiApplication
---
