---
description: ''
layout: schema
name: eventAdaptiveDataItem
properties_list:
- description: The id that was requested, ticker, cusip, factset entity id etc.
  name: requestId
  type: string
- description: Signal Id for this event.
  name: signalId
  type: string
- description: A JSON object that's compliant with MS adaptive card schema.
  name: adaptiveCard
  type: object
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-signals-event-adaptive-data-item-schema.json
slug: factset-signals-event-adaptive-data-item
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: eventAdaptiveDataItem
---
