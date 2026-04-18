---
description: Contains a password credential (client secret) associated with an application or service principal.
layout: schema
name: PasswordCredential
properties_list:
- description: ''
  name: customKeyIdentifier
  type: '[''string'', ''null'']'
- description: ''
  name: displayName
  type: '[''string'', ''null'']'
- description: The date and time at which the password expires.
  name: endDateTime
  type: string
- description: Contains the first three characters of the password.
  name: hint
  type: '[''string'', ''null'']'
- description: ''
  name: keyId
  type: string
- description: The client secret value. Only returned on creation; not retrievable afterward.
  name: secretText
  type: '[''string'', ''null'']'
- description: ''
  name: startDateTime
  type: string
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-password-credential-schema.json
slug: microsoft-graph-identity-password-credential
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
title: PasswordCredential
---
