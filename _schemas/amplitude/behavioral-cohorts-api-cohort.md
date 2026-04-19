---
description: Cohort schema from Amplitude Behavioral Cohorts API
layout: schema
name: Cohort
properties_list:
- description: The unique identifier for the cohort.
  name: id
  type: string
- description: The name of the cohort.
  name: name
  type: string
- description: A description of the cohort.
  name: description
  type: string
- description: The number of users in the cohort.
  name: size
  type: integer
- description: The date and time the cohort was last computed.
  name: lastComputed
  type: string
- description: Whether the cohort is archived.
  name: archived
  type: boolean
- description: The email of the cohort owner.
  name: owner
  type: string
- description: The Amplitude project ID the cohort belongs to.
  name: appId
  type: integer
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/behavioral-cohorts-api-cohort-schema.json
slug: behavioral-cohorts-api-cohort
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: Cohort
---
