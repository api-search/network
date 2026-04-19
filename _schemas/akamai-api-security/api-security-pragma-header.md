---
description: Describes which headers you can exclude from inspection when you pass a `Pragma` debug header.
layout: schema
name: pragma-header
properties_list:
- description: The action to perform when a user passes a `Pragma` header. The only action currently supported is `REMOVE`.
  name: action
  type: string
- description: Use `OR` to match any condition, or `AND` to match on all conditions.
  name: conditionOperator
  type: string
- description: The conditions to exclude from the default `remove` action. Any condition you set in this object appears in the `Pragma` header debug response object.
  name: excludeCondition
  type: array
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-pragma-header-schema.json
slug: api-security-pragma-header
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: pragma-header
---
