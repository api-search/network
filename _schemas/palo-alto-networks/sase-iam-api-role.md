---
description: Role schema from Palo Alto Networks SASE IAM Service API
layout: schema
name: Role
properties_list:
- description: Unique identifier of the role.
  name: id
  type: string
- description: Role name (e.g., superuser, network_admin, readonly).
  name: name
  type: string
- description: Human-readable role display name.
  name: display_name
  type: string
- description: Description of the permissions granted by this role.
  name: description
  type: string
- description: List of permission identifiers included in this role.
  name: permissions
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-iam-api-role-schema.json
slug: sase-iam-api-role
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Role
---
