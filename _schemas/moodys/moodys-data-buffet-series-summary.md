---
description: Summary metadata for a series returned in search results.
layout: schema
name: SeriesSummary
properties_list:
- description: The unique series mnemonic identifier.
  name: mnemonic
  type: string
- description: Human-readable description of the series.
  name: description
  type: string
- description: Native frequency of the series.
  name: frequency
  type: string
- description: The original data source.
  name: source
  type: string
- description: Geographic area covered by the series.
  name: geography
  type: string
- description: Data category classification.
  name: category
  type: string
- description: Earliest available observation date.
  name: startDate
  type: string
- description: Latest available observation or forecast date.
  name: endDate
  type: string
- description: Whether the series includes forecast data from Moody's Analytics models.
  name: hasForecast
  type: boolean
provider_name: Moody's
provider_slug: moodys
schema_file: json-schema/moodys-data-buffet-series-summary-schema.json
slug: moodys-data-buffet-series-summary
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
title: SeriesSummary
---
