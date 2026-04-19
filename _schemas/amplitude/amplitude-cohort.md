---
description: Schema for an Amplitude behavioral cohort representing a group of users defined by shared behavioral patterns or properties.
layout: schema
name: Amplitude Cohort
properties_list:
- description: The unique identifier for the cohort.
  name: id
  type: string
- description: The name of the cohort.
  name: name
  type: string
- description: A description of the cohort and the behavioral pattern it captures.
  name: description
  type: string
- description: The number of users currently in the cohort.
  name: size
  type: integer
- description: The date and time the cohort membership was last computed.
  name: lastComputed
  type: string
- description: Whether the cohort has been archived.
  name: archived
  type: boolean
- description: The email address of the cohort owner.
  name: owner
  type: string
- description: The Amplitude project ID the cohort belongs to.
  name: appId
  type: integer
- description: ''
  name: definition
  type: object
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/amplitude-cohort-schema.json
slug: amplitude-cohort
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: Amplitude Cohort
---
