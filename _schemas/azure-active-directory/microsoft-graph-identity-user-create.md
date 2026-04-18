---
description: Properties required when creating a new user.
layout: schema
name: UserCreate
properties_list:
- description: True if the account should be enabled.
  name: accountEnabled
  type: boolean
- description: The name to display in the address book.
  name: displayName
  type: string
- description: The mail alias for the user.
  name: mailNickname
  type: string
- description: The user principal name (user@contoso.com).
  name: userPrincipalName
  type: string
- description: ''
  name: givenName
  type: string
- description: ''
  name: surname
  type: string
- description: ''
  name: jobTitle
  type: string
- description: ''
  name: department
  type: string
- description: ''
  name: usageLocation
  type: string
- description: ''
  name: city
  type: string
- description: ''
  name: country
  type: string
- description: ''
  name: mobilePhone
  type: string
- description: ''
  name: businessPhones
  type: array
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-user-create-schema.json
slug: microsoft-graph-identity-user-create
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
title: UserCreate
---
