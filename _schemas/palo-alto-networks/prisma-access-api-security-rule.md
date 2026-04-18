---
description: SecurityRule schema from Palo Alto Networks Prisma Access Configuration API
layout: schema
name: SecurityRule
properties_list:
- description: ''
  name: id
  type: string
- description: Name of the security rule.
  name: name
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: disabled
  type: boolean
- description: Source security zones.
  name: from
  type: array
- description: Destination security zones.
  name: to
  type: array
- description: Source addresses or address groups.
  name: source
  type: array
- description: Destination addresses or address groups.
  name: destination
  type: array
- description: Source user or user group names.
  name: source_user
  type: array
- description: Applications to match.
  name: application
  type: array
- description: Services or service groups to match.
  name: service
  type: array
- description: URL categories to match.
  name: category
  type: array
- description: Action to take when the rule matches.
  name: action
  type: string
- description: ''
  name: profile_setting
  type: object
- description: Log forwarding profile name.
  name: log_setting
  type: string
- description: ''
  name: tag
  type: array
- description: ''
  name: folder
  type: string
- description: ''
  name: position
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-api-security-rule-schema.json
slug: prisma-access-api-security-rule
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: SecurityRule
---
