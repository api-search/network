---
description: ScimUser schema from Amplitude SCIM API
layout: schema
name: ScimUser
properties_list:
- description: The SCIM schema URIs for this resource.
  name: schemas
  type: array
- description: The SCIM unique identifier for the user.
  name: id
  type: string
- description: The user's email address, used as the primary identifier.
  name: userName
  type: string
- description: The user's name components.
  name: name
  type: object
- description: Array of email addresses for the user.
  name: emails
  type: array
- description: Whether the user account is active.
  name: active
  type: boolean
- description: Array of groups the user belongs to.
  name: groups
  type: array
- description: SCIM metadata for the resource.
  name: meta
  type: object
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/scim-api-scim-user-schema.json
slug: scim-api-scim-user
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: ScimUser
---
