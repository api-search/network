---
description: Contains the password profile associated with a user.
layout: schema
name: PasswordProfile
properties_list:
- description: True if the user must change their password on the next sign-in.
  name: forceChangePasswordNextSignIn
  type: boolean
- description: If true, the user must perform multi-factor authentication before being forced to change their password.
  name: forceChangePasswordNextSignInWithMfa
  type: boolean
- description: The password for the user. Must satisfy the tenant's password complexity requirements. Setting a strong password is recommended.
  name: password
  type: string
provider_name: Azure Active Directory
provider_slug: azure-active-directory
schema_file: json-schema/microsoft-graph-identity-password-profile-schema.json
slug: microsoft-graph-identity-password-profile
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
title: PasswordProfile
---
