---
description: Represents a monitoring event detected by Enterprise Manager. Events are the atomic detections that are correlated into incidents.
layout: schema
name: Event
properties_list:
- description: Unique identifier of the event.
  name: eventId
  type: string
- description: Type of the event.
  name: eventType
  type: string
- description: Severity of the event.
  name: severity
  type: string
- description: Descriptive message for the event.
  name: message
  type: string
- description: Name of the target that generated this event.
  name: targetName
  type: string
- description: Type of the target that generated this event.
  name: targetType
  type: string
- description: Name of the metric group, if this is a metric alert event.
  name: metricGroupName
  type: string
- description: Name of the metric column, if this is a metric alert event.
  name: metricColumnName
  type: string
- description: Metric value that triggered the event.
  name: metricValue
  type: number
- description: Timestamp when the event was raised.
  name: timeRaised
  type: string
- description: Timestamp when the event was resolved.
  name: timeResolved
  type: string
- description: Canonical URI for this event resource.
  name: canonicalLink
  type: string
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-cloud-control-event-schema.json
slug: oracle-enterprise-manager-cloud-control-event
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: Event
---
