---
description: HTTPSDestination schema from Palo Alto Networks Strata Logging Service API
layout: schema
name: HTTPSDestination
properties_list:
- description: Unique identifier of the HTTPS destination.
  name: destination_id
  type: string
- description: Display name of the destination.
  name: name
  type: string
- description: HTTPS endpoint URL where logs are posted.
  name: uri
  type: string
- description: HTTP method used to deliver logs.
  name: http_method
  type: string
- description: Whether TLS certificate verification is enabled.
  name: tls_verify
  type: boolean
- description: ''
  name: enabled
  type: boolean
- description: ''
  name: created_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-logging-service-api-https-destination-schema.json
slug: strata-logging-service-api-https-destination
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: HTTPSDestination
---
