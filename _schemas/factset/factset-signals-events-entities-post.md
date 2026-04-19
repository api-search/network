---
description: ''
layout: schema
name: eventsEntitiesPost
properties_list:
- description: A date/time (UTC) interval for filtering signal events based on their creation date. Defaults to NOW - 7 days if omitted. Users with limited access can only provide the default or a smaller date windo
  name: created
  type: string
- description: A date/time (UTC) interval for filtering signal events based on their last updated date. Defaults to NOW - 7 days if omitted. Users with limited access can only provide the default or a smaller date w
  name: updated
  type: string
- description: Comma delimited string of signalIds
  name: signalIds
  type: string
- description: Comma delimited string of theme ids. Full list of signal themes can be viewed at /themes.
  name: themes
  type: string
- description: Comma delimited string of category ids. Full list of signal categories can be viewed at /categories.
  name: categories
  type: string
- description: A range for filtering signal events based on their relevancy score.
  name: userRelevanceScore
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-signals-events-entities-post-schema.json
slug: factset-signals-events-entities-post
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: eventsEntitiesPost
---
