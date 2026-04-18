---
description: ZTNAApplication schema from Palo Alto Networks ZTNA Connector API
layout: schema
name: ZTNAApplication
properties_list:
- description: Unique identifier of the ZTNA application.
  name: app_id
  type: string
- description: Display name of the application.
  name: name
  type: string
- description: Description of the application.
  name: description
  type: string
- description: Connector group ID used to access this application.
  name: group_id
  type: string
- description: Fully qualified domain name of the private application.
  name: fqdn
  type: string
- description: TCP/UDP ports accessible through ZTNA.
  name: ports
  type: array
- description: Network protocols allowed for this application.
  name: protocols
  type: array
- description: Whether ZTNA access for this application is enabled.
  name: enabled
  type: boolean
- description: ''
  name: created_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/ztna-connector-api-ztna-application-schema.json
slug: ztna-connector-api-ztna-application
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ZTNAApplication
---
