---
description: SyslogDestinationRequest schema from Palo Alto Networks Strata Logging Service API
layout: schema
name: SyslogDestinationRequest
properties_list:
- description: Display name for this syslog destination.
  name: name
  type: string
- description: Syslog server hostname or IP address.
  name: server
  type: string
- description: Syslog server port number.
  name: port
  type: integer
- description: Transport protocol.
  name: protocol
  type: string
- description: ''
  name: format
  type: string
- description: ''
  name: facility
  type: string
- description: ''
  name: enabled
  type: boolean
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-logging-service-api-syslog-destination-request-schema.json
slug: strata-logging-service-api-syslog-destination-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: SyslogDestinationRequest
---
