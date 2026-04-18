---
description: Connector schema from Palo Alto Networks ZTNA Connector API
layout: schema
name: Connector
properties_list:
- description: Unique identifier of the connector.
  name: connector_id
  type: string
- description: Display name of the connector.
  name: name
  type: string
- description: ID of the connector group this connector belongs to.
  name: group_id
  type: string
- description: Current health status of the connector.
  name: status
  type: string
- description: Installed connector software version.
  name: version
  type: string
- description: Hostname of the system where the connector is installed.
  name: hostname
  type: string
- description: IP address of the connector host.
  name: ip_address
  type: string
- description: Geographic region where the connector is deployed.
  name: region
  type: string
- description: Timestamp of the connector's most recent heartbeat.
  name: last_seen_at
  type: string
- description: ''
  name: created_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/ztna-connector-api-connector-schema.json
slug: ztna-connector-api-connector
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Connector
---
