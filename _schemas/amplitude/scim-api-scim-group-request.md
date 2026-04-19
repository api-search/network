---
description: ScimGroupRequest schema from Amplitude SCIM API
layout: schema
name: ScimGroupRequest
properties_list:
- description: The SCIM schema URIs.
  name: schemas
  type: array
- description: The display name of the group.
  name: displayName
  type: string
- description: Array of initial group members.
  name: members
  type: array
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/scim-api-scim-group-request-schema.json
slug: scim-api-scim-group-request
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: ScimGroupRequest
---
