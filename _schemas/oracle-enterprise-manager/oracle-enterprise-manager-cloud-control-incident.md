---
description: Represents an incident in Enterprise Manager. Incidents are actionable issues detected by monitoring rules, correlated from one or more events.
layout: schema
name: Incident
properties_list:
- description: Unique identifier of the incident.
  name: incidentId
  type: string
- description: Brief summary of the incident.
  name: summary
  type: string
- description: Severity level of the incident.
  name: severity
  type: string
- description: Priority assigned to the incident.
  name: priority
  type: string
- description: Current status of the incident.
  name: status
  type: string
- description: Category of the incident.
  name: category
  type: string
- description: Name of the target associated with this incident.
  name: targetName
  type: string
- description: Type of the target associated with this incident.
  name: targetType
  type: string
- description: Current escalation level of the incident.
  name: escalationLevel
  type: integer
- description: Username of the incident owner or assignee.
  name: owner
  type: string
- description: Username of the person who acknowledged the incident.
  name: acknowledgedBy
  type: string
- description: Resolution state providing closure details.
  name: resolutionState
  type: string
- description: Name of the incident rule set that created this incident.
  name: ruleSetName
  type: string
- description: Timestamp when the incident was first raised.
  name: timeRaised
  type: string
- description: Timestamp of the last incident update.
  name: timeUpdated
  type: string
- description: Timestamp when the incident was resolved.
  name: timeResolved
  type: string
- description: Number of events correlated into this incident.
  name: eventCount
  type: integer
- description: Canonical URI for this incident resource.
  name: canonicalLink
  type: string
provider_name: Oracle Enterprise Manager
provider_slug: oracle-enterprise-manager
schema_file: json-schema/oracle-enterprise-manager-cloud-control-incident-schema.json
slug: oracle-enterprise-manager-cloud-control-incident
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
title: Incident
---
