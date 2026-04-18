---
description: Request body for searching events using the Events Explorer query language
layout: schema
name: EventsSearchRequest
properties_list:
- description: Filter configuration for the event search
  name: filter
  type: object
- description: Sort order for the returned events
  name: sort
  type: string
- description: Pagination settings for the event search results
  name: page
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-events-events-search-request-schema.json
slug: datadog-events-events-search-request
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: EventsSearchRequest
---
