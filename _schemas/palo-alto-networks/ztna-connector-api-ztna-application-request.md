---
description: ZTNAApplicationRequest schema from Palo Alto Networks ZTNA Connector API
layout: schema
name: ZTNAApplicationRequest
properties_list:
- description: Display name for the ZTNA application.
  name: name
  type: string
- description: Optional description of the application.
  name: description
  type: string
- description: Connector group ID to use for accessing the application.
  name: group_id
  type: string
- description: Fully qualified domain name of the private application.
  name: fqdn
  type: string
- description: TCP/UDP ports to expose through ZTNA.
  name: ports
  type: array
- description: Network protocols to allow.
  name: protocols
  type: array
- description: Whether to enable ZTNA access immediately after creation.
  name: enabled
  type: boolean
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/ztna-connector-api-ztna-application-request-schema.json
slug: ztna-connector-api-ztna-application-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ZTNAApplicationRequest
---
