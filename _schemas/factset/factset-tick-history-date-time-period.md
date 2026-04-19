---
description: 'Date-Time <p> NOTE: Using start and end parameters within dateTimeRange will fetch the data on particular days in between the timestamps given.</p>.'
layout: schema
name: dateTimePeriod
properties_list:
- description: The date for (or from which) the data is required. Supports in YYYY-MM-DDTHH:MM:SSZ format.
  name: start
  type: string
- description: The date to which data is required. Supports in YYYY-MM-DDTHH:MM:SSZ format.
  name: end
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-tick-history-date-time-period-schema.json
slug: factset-tick-history-date-time-period
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: dateTimePeriod
---
