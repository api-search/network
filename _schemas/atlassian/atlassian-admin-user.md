---
description: Represents a user account in an Atlassian organization.
layout: schema
name: User
properties_list:
- description: The unique Atlassian account identifier.
  name: account_id
  type: string
- description: The type of account.
  name: account_type
  type: string
- description: The current status of the account.
  name: account_status
  type: string
- description: The display name of the user.
  name: name
  type: string
- description: The email address of the user.
  name: email
  type: string
- description: URL of the user's profile picture.
  name: picture
  type: string
- description: The nickname of the user.
  name: nickname
  type: string
- description: The last time the user was active.
  name: last_active
  type: string
- description: When the user account was created.
  name: created
  type: string
- description: Products the user has access to.
  name: product_access
  type: array
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-admin-user-schema.json
slug: atlassian-admin-user
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: User
---
