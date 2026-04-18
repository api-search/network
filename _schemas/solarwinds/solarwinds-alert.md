---
description: Schema for a SolarWinds monitoring alert triggered by threshold violations or status changes on monitored entities.
layout: schema
name: SolarWinds Alert
properties_list:
- description: Unique identifier for the alert instance
  name: alertId
  type: integer
- description: Display name of the alert definition
  name: alertName
  type: string
- description: Alert severity level
  name: severity
  type: string
- description: Timestamp when the alert was triggered
  name: triggeredAt
  type: string
- description: Timestamp when the alert was reset, null if still active
  name: resetAt
  type:
  - string
  - 'null'
- description: Whether the alert has been acknowledged by an operator
  name: acknowledged
  type: boolean
- description: Username of the operator who acknowledged the alert
  name: acknowledgedBy
  type:
  - string
  - 'null'
- description: Alert message with details about the triggering condition
  name: message
  type: string
- description: Type of the monitored entity that triggered the alert
  name: entityType
  type: string
- description: SWIS URI of the entity that triggered the alert
  name: entityUri
  type: string
- description: Display name of the triggering entity
  name: entityCaption
  type: string
- description: ''
  name: triggerCondition
  type: object
- description: Additional notes or annotations on the alert
  name: notes
  type: string
provider_name: SolarWinds
provider_slug: solarwinds
schema_file: json-schema/solarwinds-alert-schema.json
slug: solarwinds-alert
tags:
- Application Monitoring
- Database Monitoring
- Infrastructure
- IP Address Management
- IT Management
- ITSM
- Log Management
- Network Monitoring
- Observability
title: SolarWinds Alert
---
