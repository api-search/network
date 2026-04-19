---
description: ScimGroup schema from Amplitude SCIM API
layout: schema
name: ScimGroup
properties_list:
- description: The SCIM schema URIs for this resource.
  name: schemas
  type: array
- description: The SCIM unique identifier for the group.
  name: id
  type: string
- description: The display name of the group.
  name: displayName
  type: string
- description: Array of group members.
  name: members
  type: array
- description: SCIM metadata for the resource.
  name: meta
  type: object
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/scim-api-scim-group-schema.json
slug: scim-api-scim-group
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: ScimGroup
---
