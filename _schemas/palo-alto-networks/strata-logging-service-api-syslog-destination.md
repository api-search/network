---
description: SyslogDestination schema from Palo Alto Networks Strata Logging Service API
layout: schema
name: SyslogDestination
properties_list:
- description: Unique identifier of the syslog destination.
  name: destination_id
  type: string
- description: Display name of the destination.
  name: name
  type: string
- description: Syslog server hostname or IP address.
  name: server
  type: string
- description: Syslog server port.
  name: port
  type: integer
- description: Transport protocol for syslog delivery.
  name: protocol
  type: string
- description: Syslog message format.
  name: format
  type: string
- description: Syslog facility value.
  name: facility
  type: string
- description: ''
  name: enabled
  type: boolean
- description: ''
  name: created_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-logging-service-api-syslog-destination-schema.json
slug: strata-logging-service-api-syslog-destination
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: SyslogDestination
---
