---
description: An enabled baseline for a target organizational unit.
layout: schema
name: EnabledBaseline
properties_list:
- description: The ARN of the enabled baseline.
  name: arn
  type: string
- description: The baseline ARN.
  name: baselineIdentifier
  type: string
- description: The version of the baseline.
  name: baselineVersion
  type: string
- description: ''
  name: parameters
  type: array
- description: ''
  name: statusSummary
  type: object
- description: The ARN of the target organizational unit.
  name: targetIdentifier
  type: string
provider_name: Amazon Control Tower
provider_slug: amazon-control-tower
schema_file: json-schema/enabled-baseline-schema.json
slug: enabled-baseline
tags:
- AWS
- Compliance
- Governance
- Landing Zone
- Multi-Account
- Security
- Controls
title: EnabledBaseline
---
