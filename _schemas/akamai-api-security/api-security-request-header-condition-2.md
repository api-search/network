---
description: Collects data needed for condition matches on request headers.
layout: schema
name: request-header-condition-2
properties_list:
- description: 'The type of condition. The `RequestHeaderCondition` type checks for a header from the requesting client and determines if it matches a provided header. This subtype supports the `?` wildcard to match '
  name: className
  type: string
- description: A header name. Use `name` to check whether the specified header exists.
  name: name
  type: array
- description: Whether to interpret `?` and `*` as wildcards.
  name: nameWildcard
  type: boolean
- description: Whether the condition triggers on a match or lack of match.
  name: positiveMatch
  type: boolean
- description: A list of unique header values. Use both `value` and `name` to check whether the requesting client’s header matches a provided header.
  name: value
  type: array
- description: Whether to consider the case sensitivity of the provided header values.
  name: valueCase
  type: boolean
- description: Whether to interpret `?` and `*` as wildcards.
  name: valueWildcard
  type: boolean
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-request-header-condition-2-schema.json
slug: api-security-request-header-condition-2
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: request-header-condition-2
---
