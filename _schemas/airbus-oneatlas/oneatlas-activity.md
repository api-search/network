---
description: ''
layout: schema
name: Activity
properties_list:
- description: ''
  name: _links
  type: object
- description: The time when the activity was created
  name: creationDate
  type: string
- description: The time when the activity was ended (copy of the date associated to the SUCCEEDED, CANCELED or FAILED stage)
  name: endDate
  type: string
- description: ''
  name: id
  type: object
- description: Name of the last completed stage
  name: lastStageName
  type: string
- description: A free text (copy of the last stage message)
  name: message
  type: string
- description: The copy of the origin user request
  name: payload
  type: object
- description: A priority indicator between 1 and 9. 1 is the highest.
  name: priority
  type: number
- description: A progress indicator between 0 and 100
  name: progress
  type: number
- description: The time when the activity was started (date of the first stage that is not QUEUED)
  name: startDate
  type: string
- description: Status of the activity (copy of the last stage status)
  name: status
  type: string
- description: Type of activity
  name: type
  type: string
- description: ''
  name: userId
  type: object
provider_name: Airbus OneAtlas
provider_slug: airbus-oneatlas
schema_file: json-schema/oneatlas-activity-schema.json
slug: oneatlas-activity
tags:
- Imagery
- Satellites
title: Activity
---
