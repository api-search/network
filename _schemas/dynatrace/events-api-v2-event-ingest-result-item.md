---
description: The result of ingesting an event for a single entity.
layout: schema
name: EventIngestResultItem
properties_list:
- description: The unique identifier assigned to the created event.
  name: eventId
  type: string
- description: The ingestion status for this entity. OK indicates success; other values indicate warnings or errors.
  name: status
  type: string
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/events-api-v2-event-ingest-result-item-schema.json
slug: events-api-v2-event-ingest-result-item
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
title: EventIngestResultItem
---
