---
description: Settings for an application that implements a web API
layout: schema
name: ApiApplication
properties_list:
- description: Allows an application to use claims mapping without specifying a custom signing key
  name: acceptMappedClaims
  type: '[''boolean'', ''null'']'
- description: Used for bundling consent. Lists client app IDs that are considered known clients of this API
  name: knownClientApplications
  type: array
- description: OAuth 2.0 permission scopes exposed by the web API to client applications
  name: oauth2PermissionScopes
  type: array
- description: Lists client applications pre-authorized with specified delegated permissions that do not require user consent
  name: preAuthorizedApplications
  type: array
- description: Specifies the access token version expected by the resource. Possible values are 1 or 2.
  name: requestedAccessTokenVersion
  type: '[''integer'', ''null'']'
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-graph-identity-api-application-schema.json
slug: microsoft-entra-graph-identity-api-application
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
title: ApiApplication
---
