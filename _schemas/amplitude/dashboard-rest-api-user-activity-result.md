---
description: UserActivityResult schema from Amplitude Dashboard REST API
layout: schema
name: UserActivityResult
properties_list:
- description: User metadata including user_id and Amplitude ID.
  name: userData
  type: object
- description: Array of recent events for the user.
  name: events
  type: array
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/dashboard-rest-api-user-activity-result-schema.json
slug: dashboard-rest-api-user-activity-result
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: UserActivityResult
---
