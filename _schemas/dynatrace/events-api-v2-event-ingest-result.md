---
description: The result returned after successfully ingesting a custom event.
layout: schema
name: EventIngestResult
properties_list:
- description: The number of event reports created. This may be greater than 1 if the entitySelector matched multiple entities.
  name: reportCount
  type: integer
- description: Details of each individual event ingestion result.
  name: eventIngestResults
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/events-api-v2-event-ingest-result-schema.json
slug: events-api-v2-event-ingest-result
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
title: EventIngestResult
---
