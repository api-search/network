---
description: Recommendation schema from Amplitude User Profile API
layout: schema
name: Recommendation
properties_list:
- description: The recommendation model ID.
  name: rec_id
  type: string
- description: Array of recommended item IDs.
  name: child_ids
  type: array
- description: Whether the user is in the control group for this recommendation model.
  name: is_control
  type: boolean
- description: The type of recommendation model.
  name: recommendation_type
  type: string
- description: The title of the recommendation.
  name: title
  type: string
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/user-profile-api-recommendation-schema.json
slug: user-profile-api-recommendation
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: Recommendation
---
