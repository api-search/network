---
description: UserMapping schema from Amplitude User Mapping API
layout: schema
name: UserMapping
properties_list:
- description: The primary user ID that other identities will be mapped to.
  name: global_user_id
  type: string
- description: The user ID to map to the global_user_id.
  name: user_id
  type: string
- description: When true, removes the mapping instead of creating it.
  name: unmap
  type: boolean
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/user-mapping-api-user-mapping-schema.json
slug: user-mapping-api-user-mapping
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: UserMapping
---
