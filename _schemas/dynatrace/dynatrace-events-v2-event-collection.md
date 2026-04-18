---
description: A paginated collection of events.
layout: schema
name: EventCollection
properties_list:
- description: The cursor for the next page of results. Null if there are no more pages.
  name: nextPageKey
  type: string
- description: The total number of events matching the query.
  name: totalCount
  type: integer
- description: The number of results returned on this page.
  name: pageSize
  type: integer
- description: The list of events on this page.
  name: events
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-events-v2-event-collection-schema.json
slug: dynatrace-events-v2-event-collection
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
title: EventCollection
---
