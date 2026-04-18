---
description: Event schema from Google Analytics API
layout: schema
name: Event
properties_list:
- description: The name of the event. Must not use reserved names (ad_click, app_exception, error, session_start, etc.) or reserved prefixes (_, firebase_, ga_, google_, gtag.).
  name: name
  type: string
- description: Event parameters as key-value pairs. Common parameters include session_id, engagement_time_msec, and timestamp_micros.
  name: params
  type: object
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/measurement-protocol-event-schema.json
slug: measurement-protocol-event
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: Event
---
