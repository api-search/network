---
description: An alert event representing a triggered alert condition on an SAP HANA Cloud service instance. Alerts monitor database health, resources, and operational thresholds.
layout: schema
name: AlertEvent
properties_list:
- description: The unique identifier of the alert event.
  name: alertId
  type: string
- description: The identifier of the alert rule that triggered this event.
  name: alertRuleId
  type: string
- description: The human-readable name of the alert (e.g., Memory Usage, Disk Usage, Long-Running Statements).
  name: alertName
  type: string
- description: The current state of the alert event.
  name: alertState
  type: string
- description: The severity level of the alert.
  name: severity
  type: string
- description: A detailed description of the alert condition.
  name: description
  type: string
- description: ISO 8601 timestamp when the alert was triggered.
  name: triggeredAt
  type: string
- description: ISO 8601 timestamp when the alert was resolved. Null if the alert is still active.
  name: resolvedAt
  type: string
- description: The current metric value that triggered or relates to the alert.
  name: currentValue
  type: number
- description: The threshold value configured in the alert rule.
  name: thresholdValue
  type: number
- description: The unit of measurement for the metric values (e.g., %, GB, count).
  name: unit
  type: string
- description: The service instance identifier associated with this alert.
  name: serviceInstanceId
  type: string
provider_name: SAP HANA
provider_slug: sap-hana
schema_file: json-schema/sap-hana-cloud-rest-alert-event-schema.json
slug: sap-hana-cloud-rest-alert-event
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
title: AlertEvent
---
