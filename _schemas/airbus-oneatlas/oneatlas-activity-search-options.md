---
description: ''
layout: schema
name: ActivitySearchOptions
properties_list:
- description: The creation date or creation date range of the activity
  name: creationDate
  type: object
- description: The end date pf the activity (copy of the date associated to the SUCCEEDED or FAILED stage)
  name: endDate
  type: string
- description: Number of requested items per page
  name: itemsPerPage
  type: number
- description: The copy of the origin user request. It could be the whole object or only some elements.
  name: payload
  type: object
- description: A progress indicator between 0 and 100
  name: progress
  type: number
- description: Unbounded list or parameters to sort by. The '+' indicates ascendant ordering, the '-' indicates descendant ordering. If not precised, default to '+'
  name: sortBy
  type: string
- description: The start date of the activity (date of the first stage that is not QUEUED)
  name: startDate
  type: string
- description: The index of the first item present in the response
  name: startIndex
  type: number
- description: The status or status list (comma separated list) of the activity.
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
schema_file: json-schema/oneatlas-activity-search-options-schema.json
slug: oneatlas-activity-search-options
tags:
- Imagery
- Satellites
title: ActivitySearchOptions
---
