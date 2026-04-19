---
description: Response containing a single time series with metadata and observations.
layout: schema
name: SeriesResponse
properties_list:
- description: The unique series mnemonic identifier.
  name: mnemonic
  type: string
- description: Human-readable description of the series.
  name: description
  type: string
- description: The frequency of the returned data.
  name: frequency
  type: string
- description: The original data source (e.g., BLS, BEA, IMF).
  name: source
  type: string
- description: The geographic area the series covers.
  name: geography
  type: string
- description: The unit of measurement for the series values (e.g., Billions of Chained 2017 Dollars, Thousands of Persons, Index).
  name: units
  type: string
- description: The transformation applied to the data, if any.
  name: transformation
  type: string
- description: The start date of the returned data range.
  name: startDate
  type: string
- description: The end date of the returned data range.
  name: endDate
  type: string
- description: The vintage date of the returned data.
  name: vintage
  type: string
- description: When the series was last updated in the repository.
  name: lastUpdated
  type: string
- description: Whether the series contains forecast data from Moody's Analytics models.
  name: isForecast
  type: boolean
- description: Array of date-value pairs representing the time series observations and/or forecasts.
  name: data
  type: array
provider_name: Moody's
provider_slug: moodys
schema_file: json-schema/moodys-data-buffet-series-response-schema.json
slug: moodys-data-buffet-series-response
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
title: SeriesResponse
---
