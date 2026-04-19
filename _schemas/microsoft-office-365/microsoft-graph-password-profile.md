---
description: Contains the password profile associated with a user.
layout: schema
name: PasswordProfile
properties_list:
- description: Whether the user must change the password on the next sign-in.
  name: forceChangePasswordNextSignIn
  type: boolean
- description: Whether the user must perform multi-factor authentication before being forced to change their password.
  name: forceChangePasswordNextSignInWithMfa
  type: boolean
- description: The password for the user. Must satisfy the tenant's password complexity requirements. Minimum of 8 characters.
  name: password
  type: string
provider_name: Microsoft Office 365
provider_slug: microsoft-office-365
schema_file: json-schema/microsoft-graph-password-profile-schema.json
slug: microsoft-graph-password-profile
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
title: PasswordProfile
---
