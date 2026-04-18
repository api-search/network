---
description: A security policy rule controlling traffic flow between zones based on source, destination, application, service, and user criteria.
layout: schema
name: SecurityRule
properties_list:
- description: Unique name of the security rule.
  name: '@name'
  type: string
- description: ''
  name: from
  type: object
- description: ''
  name: to
  type: object
- description: ''
  name: source
  type: object
- description: ''
  name: destination
  type: object
- description: ''
  name: source-user
  type: object
- description: ''
  name: application
  type: object
- description: ''
  name: service
  type: object
- description: ''
  name: category
  type: object
- description: Action to take on matching traffic.
  name: action
  type: string
- description: Log at session start.
  name: log-start
  type: string
- description: Log at session end.
  name: log-end
  type: string
- description: Log forwarding profile name.
  name: log-setting
  type: string
- description: Security profile group or individual profiles.
  name: profile-setting
  type: object
- description: Whether the rule is disabled.
  name: disabled
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: tag
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/pan-os-rest-api-security-rule-schema.json
slug: pan-os-rest-api-security-rule
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
