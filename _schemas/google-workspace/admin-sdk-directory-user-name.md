---
description: A user name object containing given, family, and full name.
layout: schema
name: UserName
properties_list:
- description: The user first name. Required when creating a user account.
  name: givenName
  type: string
- description: The user last name. Required when creating a user account.
  name: familyName
  type: string
- description: The user full name formed by concatenating first and last name values.
  name: fullName
  type: string
- description: The user display name.
  name: displayName
  type: string
provider_name: Google Workspace
provider_slug: google-workspace
schema_file: json-schema/admin-sdk-directory-user-name-schema.json
slug: admin-sdk-directory-user-name
tags:
- Calendar
- Collaboration
- Email
- Productivity
- Storage
- Video Conferencing
title: UserName
---
