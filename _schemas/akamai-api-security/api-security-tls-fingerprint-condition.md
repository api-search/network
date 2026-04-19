---
description: Collects data needed for condition matches on TLS fingerprints.
layout: schema
name: tls-fingerprint-condition
properties_list:
- description: The type of condition. In this case, `TlsFingerprintCondition`.
  name: className
  type: string
- description: Whether the condition triggers on a match or lack of match.
  name: positiveMatch
  type: boolean
- description: A list of unique TLS fingerprints.
  name: value
  type: array
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-tls-fingerprint-condition-schema.json
slug: api-security-tls-fingerprint-condition
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: tls-fingerprint-condition
---
