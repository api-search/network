---
description: ''
layout: schema
name: ExperienceUpdate
properties_list:
- description: The display name of the experience.
  name: name
  type: string
- description: The full description of the experience and what guests will do.
  name: description
  type: string
- description: The activity category of the experience.
  name: category
  type: string
- description: ''
  name: location
  type: object
- description: The duration of the experience in minutes.
  name: duration_minutes
  type: integer
- description: The maximum number of guests per session.
  name: max_guests
  type: integer
- description: ''
  name: pricing
  type: object
- description: The languages in which the experience is offered.
  name: languages
  type: array
- description: Items guests should bring to the experience.
  name: what_to_bring
  type: array
- description: Accessibility information for the experience.
  name: accessibility
  type: string
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-experience-update-schema.json
slug: airbnb-experience-update
tags: []
title: ExperienceUpdate
---
