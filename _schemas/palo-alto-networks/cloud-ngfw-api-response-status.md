---
description: Standard API response status envelope included in all responses.
layout: schema
name: ResponseStatus
properties_list:
- description: Error code. 0 indicates success.
  name: ErrorCode
  type: integer
- description: Human-readable status message.
  name: Reason
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cloud-ngfw-api-response-status-schema.json
slug: cloud-ngfw-api-response-status
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ResponseStatus
---
