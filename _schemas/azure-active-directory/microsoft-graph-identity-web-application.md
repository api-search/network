---
description: Configuration for a web application.
layout: schema
name: WebApplication
properties_list:
- description: Home page or landing page of the application.
  name: homePageUrl
  type: '[''string'', ''null'']'
- description: URL used by the authorization service to sign out a user.
  name: logoutUrl
  type: '[''string'', ''null'']'
- description: URIs to which Azure AD will redirect after authentication.
  name: redirectUris
  type: array
- description: ''
  name: implicitGrantSettings
  type: object
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-web-application-schema.json
slug: microsoft-graph-identity-web-application
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
title: WebApplication
---
