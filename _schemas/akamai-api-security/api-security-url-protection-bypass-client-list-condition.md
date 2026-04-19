---
description: Collects data needed for condition matches on client lists and network lists.
layout: schema
name: url-protection-bypass-client-list-condition
properties_list:
- description: __Read-only__ Whether the connecting IP or both the connecting IP and `X-Forwarded-For` (XFF) header match on the client list or network list. URL protection bypass supports `connecting` only.
  name: checkIps
  type: string
- description: Choose `NetworkListCondition` to match the requesting client's identifier, like IP, GEO, ASN or TLS Fingerprint, against the specified client list or network list.
  name: className
  type: string
- description: __Read-only__ Whether the condition triggers on a match or lack of match.
  name: positiveMatch
  type: boolean
- description: Identifies the client list or network list.
  name: value
  type: array
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-url-protection-bypass-client-list-condition-schema.json
slug: api-security-url-protection-bypass-client-list-condition
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: url-protection-bypass-client-list-condition
---
