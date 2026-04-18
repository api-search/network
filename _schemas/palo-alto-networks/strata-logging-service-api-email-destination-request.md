---
description: EmailDestinationRequest schema from Palo Alto Networks Strata Logging Service API
layout: schema
name: EmailDestinationRequest
properties_list:
- description: Display name for this email destination.
  name: name
  type: string
- description: SMTP server hostname or IP address.
  name: gateway
  type: string
- description: Sender email address.
  name: from
  type: string
- description: Primary recipient email address.
  name: to
  type: string
- description: Additional recipient email address.
  name: and_also_to
  type: string
- description: ''
  name: enabled
  type: boolean
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-logging-service-api-email-destination-request-schema.json
slug: strata-logging-service-api-email-destination-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: EmailDestinationRequest
---
