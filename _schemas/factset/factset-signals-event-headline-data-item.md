---
description: ''
layout: schema
name: eventHeadlineDataItem
properties_list:
- description: The id that was requested. This can be a ticker, cusip or factset entity id.
  name: requestId
  type: string
- description: Name of the company reported in signal. Omitted if null.
  name: companyName
  type: string
- description: Signal Id for this event. e.g. dilutionTrigger
  name: signalId
  type: string
- description: Signal Name for this event. e.g. dilutionTrigger
  name: signalName
  type: string
- description: Theme name of the signal for this event. e.g. Debt Capital Structure
  name: theme
  type: string
- description: Primary data provider for the signal this event belongs to. e.g. FactSet, Bitvore
  name: source
  type: string
- description: A unique id for this event.
  name: eventId
  type: string
- description: The UTC date/time of the event in ISO 8601 format.
  name: eventDate
  type: string
- description: One sentence summary of the event.
  name: summary
  type: string
- description: Relevancy score of this event for the requesting user on a scale of 0 to 1. Higher value indicates more relevancy.
  name: userRelevanceScore
  type: number
- description: Date/Time in UTC the event was first recorded in our data store.
  name: created
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-signals-event-headline-data-item-schema.json
slug: factset-signals-event-headline-data-item
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: eventHeadlineDataItem
---
