---
description: Collects data needed for condition matches on request headers.
layout: schema
name: url-protection-bypass-request-header-condition
properties_list:
- description: Choose `RequestHeaderCondition` to match a header from the requesting client to the specified header.
  name: className
  type: string
- description: Use `name` to check whether the specified header exists.
  name: name
  type: array
- description: Whether to interpret `?` and `*` as wildcards in the specified `name`.
  name: nameWildcard
  type: boolean
- description: __Read-only__ Whether the condition triggers on a match or lack of match.
  name: positiveMatch
  type: boolean
- description: A list of unique header values. Use both `value` and `name` to check whether the requesting client’s header matches the specified headers.
  name: value
  type: array
- description: Whether to consider case when matching header values, `true` for case-sensitive matches.
  name: valueCase
  type: boolean
- description: Whether to interpret `?` and `*` as wildcards in the specified `value`.
  name: valueWildcard
  type: boolean
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-url-protection-bypass-request-header-condition-schema.json
slug: api-security-url-protection-bypass-request-header-condition
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: url-protection-bypass-request-header-condition
---
