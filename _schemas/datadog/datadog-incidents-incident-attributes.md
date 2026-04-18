---
description: The attributes of an incident record
layout: schema
name: IncidentAttributes
properties_list:
- description: The title of the incident describing what is affected
  name: title
  type: string
- description: The sequential human-readable public ID of the incident within the organization
  name: public_id
  type: integer
- description: The current state of the incident in its lifecycle
  name: state
  type: string
- description: The severity level of the incident
  name: severity
  type: string
- description: Whether the incident is causing direct customer impact
  name: customer_impacted
  type: boolean
- description: Description of the scope of customer impact for this incident
  name: customer_impact_scope
  type: string
- description: ISO 8601 timestamp when customer impact began
  name: customer_impact_start
  type: string
- description: ISO 8601 timestamp when customer impact ended
  name: customer_impact_end
  type: string
- description: Duration of customer impact in seconds
  name: customer_impact_duration
  type: integer
- description: ISO 8601 timestamp when the incident was created
  name: created
  type: string
- description: ISO 8601 timestamp when the incident was last modified
  name: modified
  type: string
- description: ISO 8601 timestamp when the incident was first detected
  name: detected
  type: string
- description: ISO 8601 timestamp when the incident was marked as resolved
  name: resolved
  type: string
- description: Time in seconds from incident start to detection
  name: time_to_detect
  type: integer
- description: Time in seconds from detection to first responder acknowledgement
  name: time_to_internal_response
  type: integer
- description: Time in seconds from detection to resolution
  name: time_to_repair
  type: integer
- description: Custom field values for the incident as defined in organization settings
  name: fields
  type: object
- description: List of notification handles that were paged for this incident
  name: notification_handles
  type: array
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-incidents-incident-attributes-schema.json
slug: datadog-incidents-incident-attributes
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: IncidentAttributes
---
