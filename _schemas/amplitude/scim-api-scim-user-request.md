---
description: ScimUserRequest schema from Amplitude SCIM API
layout: schema
name: ScimUserRequest
properties_list:
- description: The SCIM schema URIs, typically urn:ietf:params:scim:schemas:core:2.0:User.
  name: schemas
  type: array
- description: The user's email address.
  name: userName
  type: string
- description: ''
  name: name
  type: object
- description: ''
  name: emails
  type: array
- description: Whether the user account should be active.
  name: active
  type: boolean
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/scim-api-scim-user-request-schema.json
slug: scim-api-scim-user-request
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: ScimUserRequest
---
