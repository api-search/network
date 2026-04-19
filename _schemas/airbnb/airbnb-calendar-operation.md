---
description: ''
layout: schema
name: CalendarOperation
properties_list:
- description: The start date of the range to update.
  name: start_date
  type: string
- description: The end date of the range to update.
  name: end_date
  type: string
- description: Whether the dates should be available or blocked.
  name: available
  type: boolean
- description: The nightly price to set for this date range.
  name: price
  type: number
- description: The minimum number of nights required for stays in this range.
  name: minimum_nights
  type: integer
- description: The maximum number of nights allowed for stays in this range.
  name: maximum_nights
  type: integer
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-calendar-operation-schema.json
slug: airbnb-calendar-operation
tags: []
title: CalendarOperation
---
