---
description: Incident schema from Palo Alto Networks SaaS Security API
layout: schema
name: Incident
properties_list:
- description: Unique incident identifier.
  name: id
  type: string
- description: Summary title of the incident.
  name: title
  type: string
- description: Detailed description of the security incident.
  name: description
  type: string
- description: Current incident status.
  name: status
  type: string
- description: Incident severity level.
  name: severity
  type: string
- description: ID of the SaaS application where the incident occurred.
  name: app_id
  type: string
- description: Name of the SaaS application.
  name: app_name
  type: string
- description: Name of the policy that triggered the incident.
  name: policy_name
  type: string
- description: IDs of assets involved in the incident.
  name: affected_assets
  type: array
- description: User IDs of users involved in the incident.
  name: affected_users
  type: array
- description: User ID of the assigned analyst.
  name: assignee_id
  type: string
- description: Timestamp when the incident was detected.
  name: created_at
  type: string
- description: Timestamp of the most recent update.
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/saas-security-api-incident-schema.json
slug: saas-security-api-incident
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Incident
---
