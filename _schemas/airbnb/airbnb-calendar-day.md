---
description: ''
layout: schema
name: CalendarDay
properties_list:
- description: The date for this calendar entry.
  name: date
  type: string
- description: Whether the listing is available for booking on this date.
  name: available
  type: boolean
- description: The nightly price for this date in the listing currency.
  name: price
  type: number
- description: The minimum number of nights required for a stay starting on this date.
  name: minimum_nights
  type: integer
- description: The maximum number of nights allowed for a stay starting on this date.
  name: maximum_nights
  type: integer
- description: The reservation identifier if this date is booked.
  name: reservation_id
  type: string
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-calendar-day-schema.json
slug: airbnb-calendar-day
tags: []
title: CalendarDay
---
