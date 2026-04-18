---
description: Attributes for creating a new incident
layout: schema
name: IncidentCreateAttributes
properties_list:
- description: The title of the incident describing what is affected and the nature of the issue
  name: title
  type: string
- description: Whether the incident is causing direct customer impact (required field for all incidents)
  name: customer_impacted
  type: boolean
- description: Description of the customer groups or features affected by this incident
  name: customer_impact_scope
  type: string
- description: ISO 8601 timestamp when customer impact started, if known
  name: customer_impact_start
  type: string
- description: The severity level of the incident using SEV-N notation
  name: severity
  type: string
- description: The initial state of the incident
  name: state
  type: string
- description: Custom fields for the incident as configured in your organization settings
  name: fields
  type: object
- description: List of user and team notification handles to page on incident creation
  name: notification_handles
  type: array
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-incidents-incident-create-attributes-schema.json
slug: datadog-incidents-incident-create-attributes
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: IncidentCreateAttributes
---
