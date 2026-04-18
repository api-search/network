---
description: Detailed information about a SASE security incident for enrichment and correlation.
layout: schema
name: IncidentDetail
properties_list:
- description: Unique incident identifier.
  name: incidentId
  type: string
- description: Incident type classification.
  name: type
  type: string
- description: ''
  name: severity
  type: string
- description: Incident title.
  name: title
  type: string
- description: Incident description.
  name: description
  type: string
- description: Tenant Service Group identifier.
  name: tsg_id
  type: string
- description: Incident category.
  name: category
  type: string
- description: Source of the incident detection.
  name: detectionSource
  type: string
- description: ''
  name: timestamp
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-notifications-incident-detail-schema.json
slug: sase-notifications-incident-detail
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: IncidentDetail
---
