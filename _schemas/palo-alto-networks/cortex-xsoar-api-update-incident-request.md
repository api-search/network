---
description: UpdateIncidentRequest schema from Palo Alto Networks Cortex XSOAR REST API
layout: schema
name: UpdateIncidentRequest
properties_list:
- description: ID of the incident to update.
  name: id
  type: string
- description: Incident version for optimistic locking. Retrieve from a prior GET request.
  name: version
  type: integer
- description: ''
  name: status
  type: integer
- description: ''
  name: severity
  type: integer
- description: ''
  name: owner
  type: string
- description: ''
  name: details
  type: string
- description: ''
  name: closeReason
  type: string
- description: ''
  name: closeNotes
  type: string
- description: ''
  name: CustomFields
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsoar-api-update-incident-request-schema.json
slug: cortex-xsoar-api-update-incident-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: UpdateIncidentRequest
---
