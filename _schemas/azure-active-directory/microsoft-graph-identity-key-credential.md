---
description: Contains a key credential (certificate) associated with an application or service principal.
layout: schema
name: KeyCredential
properties_list:
- description: Custom key identifier.
  name: customKeyIdentifier
  type: '[''string'', ''null'']'
- description: ''
  name: displayName
  type: '[''string'', ''null'']'
- description: The date and time at which the credential expires.
  name: endDateTime
  type: string
- description: The certificate raw data in byte array converted to Base64 string.
  name: key
  type: '[''string'', ''null'']'
- description: ''
  name: keyId
  type: string
- description: ''
  name: startDateTime
  type: string
- description: The type of key credential (e.g., AsymmetricX509Cert).
  name: type
  type: string
- description: Describes the purpose of the key. Valid values are Verify and Sign.
  name: usage
  type: string
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-key-credential-schema.json
slug: microsoft-graph-identity-key-credential
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
title: KeyCredential
---
