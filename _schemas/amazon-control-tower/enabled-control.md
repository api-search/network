---
description: Information about an enabled control.
layout: schema
name: EnabledControl
properties_list:
- description: The ARN of the enabled control.
  name: arn
  type: string
- description: The control identifier.
  name: controlIdentifier
  type: string
- description: ''
  name: driftStatusSummary
  type: object
- description: ''
  name: parameters
  type: array
- description: ''
  name: statusSummary
  type: object
- description: The ARN of the organizational unit.
  name: targetIdentifier
  type: string
provider_name: Amazon Control Tower
provider_slug: amazon-control-tower
schema_file: json-schema/enabled-control-schema.json
slug: enabled-control
tags:
- AWS
- Compliance
- Governance
- Landing Zone
- Multi-Account
- Security
- Controls
title: EnabledControl
---
