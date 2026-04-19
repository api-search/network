---
description: Contains the password profile associated with a user. The passwordProfile property of the user entity is a passwordProfile object.
layout: schema
name: PasswordProfile
properties_list:
- description: The password for the user. Must satisfy the password complexity requirements of the tenant. Required on create.
  name: password
  type: string
- description: true if the user must change the password on the next sign-in; false otherwise
  name: forceChangePasswordNextSignIn
  type: boolean
- description: true if the user must perform multi-factor authentication before being forced to change the password
  name: forceChangePasswordNextSignInWithMfa
  type: boolean
provider_name: Microsoft Entra
provider_slug: microsoft-entra
schema_file: json-schema/microsoft-entra-graph-identity-password-profile-schema.json
slug: microsoft-entra-graph-identity-password-profile
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
title: PasswordProfile
---
