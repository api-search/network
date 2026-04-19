---
description: ''
layout: schema
name: rollover
properties_list:
- description: Time of last zero date rollover for the Americas. This is in Eastern Time Zone. The date-time format is expressed as [YYYY-MM-DD]T[HH:MM:SSS], following ISO 8601.
  name: americasRollTime
  type: string
- description: Current relative zero date for the Americas. Date is expressed in Eastern Time and expressed as YYYY-MM-DD.
  name: americasZeroDate
  type: string
- description: Time of last zero date rollover for Asia/Pacific. This is in Eastern Time Zone. The date-time format is expressed as [YYYY-MM-DD]T[HH:MM:SSS], following ISO 8601.
  name: asiapacificRollTime
  type: string
- description: Current relative zero date for Asia/Pacific. This is in Eastern Time Zone
  name: asiapacificZeroDate
  type: string
- description: Time of last zero date rollover for Europe. This is in Eastern Time Zone. The date-time format is expressed as [YYYY-MM-DD]T[HH:MM:SSS], following ISO 8601.
  name: europeRollTime
  type: string
- description: Current relative zero date for Europe. This is in Eastern Time Zone
  name: europeZeroDate
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-prices-rollover-schema.json
slug: factset-prices-rollover
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: rollover
---
