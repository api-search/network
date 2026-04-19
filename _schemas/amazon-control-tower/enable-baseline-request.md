---
description: EnableBaselineRequest schema from AWS Control Tower API
layout: schema
name: EnableBaselineRequest
properties_list:
- description: The ARN of the baseline.
  name: baselineIdentifier
  type: string
- description: The specific version to be enabled.
  name: baselineVersion
  type: string
- description: A list of key-value objects that specify enablement parameters.
  name: parameters
  type: array
- description: Tags to apply to the EnabledBaseline resource.
  name: tags
  type: object
- description: The ARN of the target organizational unit.
  name: targetIdentifier
  type: string
provider_name: Amazon Control Tower
provider_slug: amazon-control-tower
schema_file: json-schema/enable-baseline-request-schema.json
slug: enable-baseline-request
tags:
- AWS
- Compliance
- Governance
- Landing Zone
- Multi-Account
- Security
- Controls
title: EnableBaselineRequest
---
