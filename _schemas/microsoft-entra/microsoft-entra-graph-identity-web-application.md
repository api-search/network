---
description: Web application configuration including redirect URIs
layout: schema
name: WebApplication
properties_list:
- description: URIs to which Microsoft Entra ID will redirect after authentication
  name: redirectUris
  type: array
- description: Home page URL of the application
  name: homePageUrl
  type: '[''string'', ''null'']'
- description: URL used by the authorization service to sign out the user
  name: logoutUrl
  type: '[''string'', ''null'']'
- description: Settings for implicit grant flow tokens
  name: implicitGrantSettings
  type: object
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-graph-identity-web-application-schema.json
slug: microsoft-entra-graph-identity-web-application
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
title: WebApplication
---
