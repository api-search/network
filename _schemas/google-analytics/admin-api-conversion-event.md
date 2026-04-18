---
description: A conversion event in a Google Analytics property.
layout: schema
name: ConversionEvent
properties_list:
- description: Optional. The method by which conversions will be counted across multiple events within a session. If this value is not provided, it will be set to `ONCE_PER_EVENT`.
  name: countingMethod
  type: string
- description: Output only. Time when this conversion event was created in the property.
  name: createTime
  type: string
- description: Output only. If set to true, this conversion event refers to a custom event. If set to false, this conversion event refers to a default event in GA. Default events typically have special meaning in GA
  name: custom
  type: boolean
- description: Defines a default value/currency for a conversion event. Both value and currency must be provided.
  name: defaultConversionValue
  type: object
- description: Output only. If set, this event can currently be deleted with DeleteConversionEvent.
  name: deletable
  type: boolean
- description: 'Immutable. The event name for this conversion event. Examples: ''click'', ''purchase'''
  name: eventName
  type: string
- description: 'Output only. Resource name of this conversion event. Format: properties/{property}/conversionEvents/{conversion_event}'
  name: name
  type: string
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/admin-api-conversion-event-schema.json
slug: admin-api-conversion-event
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: ConversionEvent
---
