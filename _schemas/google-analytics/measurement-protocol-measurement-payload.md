---
description: MeasurementPayload schema from Google Analytics API
layout: schema
name: MeasurementPayload
properties_list:
- description: Uniquely identifies a user instance of a web client. Required for web streams.
  name: client_id
  type: string
- description: Uniquely identifies a user instance of an app. Required for app streams.
  name: app_instance_id
  type: string
- description: A unique identifier for a user. Enables cross-platform analysis. Must contain only UTF-8 characters.
  name: user_id
  type: string
- description: Unix timestamp in microseconds for the request. Used to backdate events up to 72 hours.
  name: timestamp_micros
  type: integer
- description: User-scoped properties for the measurement.
  name: user_properties
  type: object
- description: User-provided data for enhanced measurement.
  name: user_data
  type: object
- description: ''
  name: consent
  type: object
- description: Deprecated. Use consent.ad_personalization instead.
  name: non_personalized_ads
  type: boolean
- description: ''
  name: user_location
  type: object
- description: IP address used to derive geographic information.
  name: ip_override
  type: string
- description: ''
  name: device
  type: object
- description: Controls validation strictness. RELAXED only rejects malformed requests. ENFORCE_RECOMMENDATIONS also rejects invalid types and exceeded limits.
  name: validation_behavior
  type: string
- description: Array of event objects. Maximum 25 events per request.
  name: events
  type: array
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/measurement-protocol-measurement-payload-schema.json
slug: measurement-protocol-measurement-payload
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: MeasurementPayload
---
