---
description: UserData schema from Amplitude User Profile API
layout: schema
name: UserData
properties_list:
- description: The user's user_id.
  name: user_id
  type: string
- description: A dictionary of the user's properties as set via the Identify API or SDK.
  name: user_properties
  type: object
- description: A dictionary of computed properties calculated by Amplitude for the user.
  name: computed_properties
  type: object
- description: Array of cohort IDs the user is a member of.
  name: cohort_ids
  type: array
- description: Array of personalized recommendation results for the user. Only included when get_recs is true.
  name: recommendations
  type: array
- description: The Amplitude internal ID for the user.
  name: amplitude_id
  type: integer
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/user-profile-api-user-data-schema.json
slug: user-profile-api-user-data
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: UserData
---
