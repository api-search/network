---
description: EnableControlRequest schema from AWS Control Tower API
layout: schema
name: EnableControlRequest
properties_list:
- description: The ARN of the control. Only Strongly recommended and Elective controls are permitted.
  name: controlIdentifier
  type: string
- description: The ARN of the organizational unit on which the control will be enabled.
  name: targetIdentifier
  type: string
- description: A list of input parameter values that are supplied to enable the control.
  name: parameters
  type: array
- description: Tags to apply to the EnabledControl resource.
  name: tags
  type: object
provider_name: Amazon Control Tower
provider_slug: amazon-control-tower
schema_file: json-schema/enable-control-request-schema.json
slug: enable-control-request
tags:
- AWS
- Compliance
- Governance
- Landing Zone
- Multi-Account
- Security
- Controls
title: EnableControlRequest
---
