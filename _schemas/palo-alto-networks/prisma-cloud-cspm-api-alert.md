---
description: Alert schema from Palo Alto Networks Prisma Cloud CSPM API
layout: schema
name: Alert
properties_list:
- description: Unique alert identifier.
  name: id
  type: string
- description: Current alert status.
  name: status
  type: string
- description: Reason for the current alert status.
  name: reason
  type: string
- description: Epoch timestamp in milliseconds when the alert was first generated.
  name: firstSeen
  type: integer
- description: Epoch timestamp in milliseconds when the alert was last seen.
  name: lastSeen
  type: integer
- description: Epoch timestamp in milliseconds of the alert.
  name: alertTime
  type: integer
- description: Policy that generated this alert.
  name: policy
  type: object
- description: Cloud resource associated with the alert.
  name: resource
  type: object
- description: ''
  name: riskDetail
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-cspm-api-alert-schema.json
slug: prisma-cloud-cspm-api-alert
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Alert
---
