---
description: A security policy rule defining traffic matching criteria and enforcement action applied by managed firewalls.
layout: schema
name: SecurityRule
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: name
  type: string
- description: ''
  name: folder
  type: string
- description: ''
  name: position
  type: string
- description: Source security zones.
  name: from
  type: array
- description: Destination security zones.
  name: to
  type: array
- description: Source addresses or address groups (use "any" for all).
  name: source
  type: array
- description: Destination addresses or address groups.
  name: destination
  type: array
- description: Source users or user groups.
  name: source_user
  type: array
- description: Applications to match (e.g., ssl, web-browsing).
  name: application
  type: array
- description: Service objects or application-default.
  name: service
  type: array
- description: URL categories to match.
  name: category
  type: array
- description: ''
  name: action
  type: string
- description: Log forwarding profile name.
  name: log_setting
  type: string
- description: ''
  name: profile_setting
  type: object
- description: ''
  name: disabled
  type: boolean
- description: ''
  name: description
  type: string
- description: ''
  name: tag
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-cloud-manager-api-security-rule-schema.json
slug: strata-cloud-manager-api-security-rule
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
