---
description: ConnectorGroup schema from Palo Alto Networks ZTNA Connector API
layout: schema
name: ConnectorGroup
properties_list:
- description: Unique identifier of the connector group.
  name: group_id
  type: string
- description: Display name of the connector group.
  name: name
  type: string
- description: Description of the connector group's purpose.
  name: description
  type: string
- description: Number of connectors in this group.
  name: connector_count
  type: integer
- description: Primary geographic region for this connector group.
  name: region
  type: string
- description: ''
  name: created_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/ztna-connector-api-connector-group-schema.json
slug: ztna-connector-api-connector-group
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ConnectorGroup
---
