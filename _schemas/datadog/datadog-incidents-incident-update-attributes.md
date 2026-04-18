---
description: Attributes to update on an existing incident
layout: schema
name: IncidentUpdateAttributes
properties_list:
- description: The updated title of the incident
  name: title
  type: string
- description: The updated state of the incident (transitioning to resolved records resolution time)
  name: state
  type: string
- description: The updated severity level of the incident
  name: severity
  type: string
- description: Updated flag indicating whether the incident has customer impact
  name: customer_impacted
  type: boolean
- description: Updated description of the customer impact scope
  name: customer_impact_scope
  type: string
- description: ISO 8601 timestamp when customer impact ended (set when marking impact as resolved)
  name: customer_impact_end
  type: string
- description: Updated custom field values for the incident
  name: fields
  type: object
- description: Updated list of notification handles for the incident
  name: notification_handles
  type: array
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-incidents-incident-update-attributes-schema.json
slug: datadog-incidents-incident-update-attributes
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: IncidentUpdateAttributes
---
