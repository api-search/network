---
description: HTTPSDestinationRequest schema from Palo Alto Networks Strata Logging Service API
layout: schema
name: HTTPSDestinationRequest
properties_list:
- description: Display name for this HTTPS destination.
  name: name
  type: string
- description: HTTPS endpoint URL.
  name: uri
  type: string
- description: ''
  name: http_method
  type: string
- description: Additional HTTP headers to include in log delivery requests.
  name: headers
  type: object
- description: ''
  name: tls_verify
  type: boolean
- description: ''
  name: enabled
  type: boolean
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-logging-service-api-https-destination-request-schema.json
slug: strata-logging-service-api-https-destination-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: HTTPSDestinationRequest
---
