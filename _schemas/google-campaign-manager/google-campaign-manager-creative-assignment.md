---
description: Creative assignment within a creative rotation.
layout: schema
name: CreativeAssignment
properties_list:
- description: ID of the creative to be assigned.
  name: creativeId
  type: string
- description: Whether this creative assignment is active.
  name: active
  type: boolean
- description: Weight of the creative assignment.
  name: weight
  type: integer
- description: ''
  name: startTime
  type: string
- description: ''
  name: endTime
  type: string
- description: Sequence number of the creative assignment.
  name: sequence
  type: integer
- description: ''
  name: richMediaExitOverrides
  type: array
provider_name: Google Campaign Manager
provider_slug: google-campaign-manager
schema_file: json-schema/google-campaign-manager-creative-assignment-schema.json
slug: google-campaign-manager-creative-assignment
tags:
- Advertising
- Analytics
- Campaign Management
- Digital Marketing
- Reporting
title: CreativeAssignment
---
