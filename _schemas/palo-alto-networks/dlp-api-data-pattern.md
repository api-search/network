---
description: DataPattern schema from Palo Alto Networks Enterprise DLP API
layout: schema
name: DataPattern
properties_list:
- description: Unique data pattern identifier.
  name: id
  type: string
- description: Display name of the data pattern.
  name: name
  type: string
- description: Human-readable description of what the pattern detects.
  name: description
  type: string
- description: Whether the pattern is predefined or custom.
  name: type
  type: string
- description: Pattern category (e.g., PII, PCI, HIPAA, Financial).
  name: category
  type: string
- description: Confidence threshold for the pattern.
  name: confidence
  type: string
- description: Detection rule definitions for the pattern.
  name: detection_rules
  type: array
- description: Whether the data pattern is active.
  name: enabled
  type: boolean
- description: Total number of incidents triggered by this pattern.
  name: incident_count
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/dlp-api-data-pattern-schema.json
slug: dlp-api-data-pattern
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: DataPattern
---
