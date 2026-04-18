---
description: Response containing a paginated list of events from the Events Explorer
layout: schema
name: EventsListResponse
properties_list:
- description: List of event objects matching the search criteria
  name: data
  type: array
- description: Pagination links for navigating through the result set
  name: links
  type: object
- description: Metadata about the event list response
  name: meta
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-events-events-list-response-schema.json
slug: datadog-events-events-list-response
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: EventsListResponse
---
