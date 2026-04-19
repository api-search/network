---
description: A security event report for a business site.
layout: schema
name: EventReport
properties_list:
- description: Site ID.
  name: siteId
  type: string
- description: Report time period.
  name: period
  type: object
- description: Summary statistics.
  name: summary
  type: object
- description: List of events in the period.
  name: events
  type: array
provider_name: ADT
provider_slug: adt
schema_file: json-schema/business-api-event-report-schema.json
slug: business-api-event-report
tags:
- Access Control
- Automation
- Home Security
- IoT
- Monitoring
- Security
- Smart Home
title: EventReport
---
