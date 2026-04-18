---
description: A Cortex XSOAR incident representing a security event under investigation.
layout: schema
name: Incident
properties_list:
- description: Unique incident identifier.
  name: id
  type: string
- description: Incident name or title.
  name: name
  type: string
- description: Incident type (maps to an incident type definition).
  name: type
  type: string
- description: 'Incident status code: 0 (Pending), 1 (Active), 2 (Done), 3 (Archive).'
  name: status
  type: integer
- description: 'Severity level: 0 (Unknown), 1 (Informational), 2 (Low), 3 (Medium), 4 (High), 5 (Critical).'
  name: severity
  type: integer
- description: Username of the analyst assigned to this incident.
  name: owner
  type: string
- description: Incident creation timestamp.
  name: created
  type: string
- description: Last modification timestamp.
  name: modified
  type: string
- description: Timestamp when the security event occurred.
  name: occurred
  type: string
- description: Incident closure timestamp.
  name: closed
  type: string
- description: Reason for closing the incident.
  name: closeReason
  type: string
- description: Notes added when closing the incident.
  name: closeNotes
  type: string
- description: Key-value label pairs attached to the incident.
  name: labels
  type: array
- description: Incident details or description.
  name: details
  type: string
- description: Associated investigation ID.
  name: investigationId
  type: string
- description: Playbook assigned to this incident.
  name: playbookId
  type: string
- description: Integration instance that created this incident.
  name: sourceInstance
  type: string
- description: Integration brand that created this incident.
  name: sourceBrand
  type: string
- description: Raw JSON payload from the originating event.
  name: rawJson
  type: string
- description: Custom field values specific to the incident type.
  name: CustomFields
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsoar-api-incident-schema.json
slug: cortex-xsoar-api-incident
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
