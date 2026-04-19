---
description: An alert rule defining the condition and threshold that triggers an alert for an SAP HANA Cloud service instance. Rules can be cloud-native or embedded statistics server (ESS) based.
layout: schema
name: AlertRule
properties_list:
- description: The unique identifier of the alert rule.
  name: ruleId
  type: string
- description: The human-readable name of the alert rule (e.g., Memory Usage Alert, Disk Full Alert).
  name: ruleName
  type: string
- description: The type of alert rule.
  name: ruleType
  type: string
- description: Whether the alert rule is currently active.
  name: enabled
  type: boolean
- description: The severity level assigned to alerts triggered by this rule.
  name: severity
  type: string
- description: The metric being monitored by this rule.
  name: metric
  type: string
- description: The comparison operator used to evaluate the threshold.
  name: thresholdOperator
  type: string
- description: The threshold value that triggers the alert when exceeded.
  name: thresholdValue
  type: number
- description: The unit of measurement for the threshold value.
  name: unit
  type: string
- description: A description of what this alert rule monitors.
  name: description
  type: string
provider_name: SAP HANA
provider_slug: sap-hana
schema_file: json-schema/sap-hana-cloud-rest-alert-rule-schema.json
slug: sap-hana-cloud-rest-alert-rule
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
title: AlertRule
---
