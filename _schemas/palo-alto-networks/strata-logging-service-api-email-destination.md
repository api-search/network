---
description: EmailDestination schema from Palo Alto Networks Strata Logging Service API
layout: schema
name: EmailDestination
properties_list:
- description: Unique identifier of the email destination.
  name: destination_id
  type: string
- description: Display name of the destination.
  name: name
  type: string
- description: SMTP server hostname.
  name: gateway
  type: string
- description: Sender email address.
  name: from
  type: string
- description: Recipient email address.
  name: to
  type: string
- description: Additional recipient email address.
  name: and_also_to
  type: string
- description: ''
  name: enabled
  type: boolean
- description: ''
  name: created_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-logging-service-api-email-destination-schema.json
slug: strata-logging-service-api-email-destination
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: EmailDestination
---
