---
description: The time period during which the custom rule is active.
layout: schema
name: effectiveTimePeriod
properties_list:
- description: An ISO 8601 timestamp that sets when the rule expires or deactivates.
  name: endDate
  type: string
- description: An ISO 8601 timestamp that sets when the rule activates.
  name: startDate
  type: string
- description: The current status of the rule based on its `startDate` and `endDate`. By default, rules are active for 30 days. When `ACTIVE`, the rule triggers when conditions are met. When `INACTIVE`, the rule doe
  name: status
  type: string
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-effective-time-period-schema.json
slug: api-security-effective-time-period
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: effectiveTimePeriod
---
