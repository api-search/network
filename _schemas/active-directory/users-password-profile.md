---
description: Password profile for a Microsoft Entra user account
layout: schema
name: PasswordProfile
properties_list:
- description: Password for the user — must meet tenant complexity requirements
  name: password
  type: string
- description: If true, user must reset password at next sign-in
  name: forceChangePasswordNextSignIn
  type: boolean
- description: If true, user must perform MFA and then reset password at next sign-in
  name: forceChangePasswordNextSignInWithMfa
  type: boolean
provider_name: Microsoft Active Directory
provider_slug: active-directory
schema_file: json-schema/users-password-profile-schema.json
slug: users-password-profile
tags:
- Active Directory
- Authentication
- Authorization
- Directory Services
- Identity Management
- Microsoft Entra
- Zero Trust
title: PasswordProfile
---
