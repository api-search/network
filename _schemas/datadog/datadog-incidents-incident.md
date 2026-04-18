---
description: A Datadog incident record representing an outage or service disruption
layout: schema
name: Incident
properties_list:
- description: The unique string identifier of the incident
  name: id
  type: string
- description: The resource type identifier (always 'incidents')
  name: type
  type: string
- description: ''
  name: attributes
  type: object
- description: Relationships to associated resources such as commander, teams, and services
  name: relationships
  type: object
provider_name: Datadog
provider_slug: datadog
schema_file: json-schema/datadog-incidents-incident-schema.json
slug: datadog-incidents-incident
tags:
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
title: Incident
---
