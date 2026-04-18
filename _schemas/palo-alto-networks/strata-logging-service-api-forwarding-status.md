---
description: ForwardingStatus schema from Palo Alto Networks Strata Logging Service API
layout: schema
name: ForwardingStatus
properties_list:
- description: Log forwarding profile identifier.
  name: profile_id
  type: string
- description: Overall health status of the forwarding profile.
  name: overall_status
  type: string
- description: Per-destination status details.
  name: destinations
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-logging-service-api-forwarding-status-schema.json
slug: strata-logging-service-api-forwarding-status
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ForwardingStatus
---
