---
description: A single time series observation or forecast data point.
layout: schema
name: Observation
properties_list:
- description: The observation date in YYYY-MM-DD format. For frequencies coarser than daily, represents the period start date.
  name: date
  type: string
- description: The observation value. Null indicates missing or unavailable data for this period.
  name: value
  type: '[''number'', ''null'']'
- description: Status indicator for the data point.
  name: status
  type: string
provider_name: Moody's
provider_slug: moodys
schema_file: json-schema/moodys-data-buffet-observation-schema.json
slug: moodys-data-buffet-observation
tags:
- Climate Risk
- Compliance
- Credit Risk
- Economic Data
- Entity Verification
- Financial Analytics
- Insurance
- KYC
- Risk
- Screening
title: Observation
---
