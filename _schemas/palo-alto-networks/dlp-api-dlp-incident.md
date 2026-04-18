---
description: DLPIncident schema from Palo Alto Networks Enterprise DLP API
layout: schema
name: DLPIncident
properties_list:
- description: Unique incident identifier.
  name: incident_id
  type: string
- description: Current incident status.
  name: status
  type: string
- description: Incident severity level.
  name: severity
  type: string
- description: Name of the data pattern that triggered the incident.
  name: data_pattern_name
  type: string
- description: Identifier of the data pattern that triggered the incident.
  name: data_pattern_id
  type: string
- description: Number of data pattern matches in the content.
  name: match_count
  type: integer
- description: Channel where the data exposure was detected.
  name: channel
  type: string
- description: Email address or username of the user involved.
  name: user
  type: string
- description: Timestamp when the incident was detected.
  name: timestamp
  type: string
- description: Application associated with the incident.
  name: application
  type: string
- description: Name of the file containing sensitive data.
  name: file_name
  type: string
- description: MIME type of the file.
  name: file_type
  type: string
- description: Size of the file in bytes.
  name: file_size
  type: integer
- description: Direction of data movement.
  name: direction
  type: string
- description: Automated action taken on the incident.
  name: action_taken
  type: string
- description: Comments added by the reviewing analyst.
  name: reviewer_comments
  type: string
- description: Email address of the analyst who reviewed the incident.
  name: reviewed_by
  type: string
- description: Timestamp when the incident was last reviewed.
  name: reviewed_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/dlp-api-dlp-incident-schema.json
slug: dlp-api-dlp-incident
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: DLPIncident
---
