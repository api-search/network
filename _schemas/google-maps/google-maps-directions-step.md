---
description: A single step of a route leg
layout: schema
name: Step
properties_list:
- description: Formatted instructions for this step, presented as an HTML text string.
  name: html_instructions
  type: string
- description: The travel mode for this step
  name: travel_mode
  type: string
- description: The maneuver action for this step (e.g., turn-left, roundabout-right, merge, straight, etc.).
  name: maneuver
  type: string
- description: Sub-steps for walking or transit legs in multi-modal routes
  name: steps
  type: array
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-directions-step-schema.json
slug: google-maps-directions-step
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: Step
---
