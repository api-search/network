---
description: The PUT Request JSON for Prefetch Requests.
layout: schema
name: prefetch-request-put
properties_list:
- description: Whether to enable prefetch requests for all extensions.
  name: allExtensions
  type: boolean
- description: Whether to enable Prefetch Requests.
  name: enableAppLayer
  type: boolean
- description: Whether to enable Prefetch Requests for rate controls.
  name: enableRateControls
  type: boolean
- description: List of extensions.
  name: extensions
  type: array
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-prefetch-request-put-schema.json
slug: api-security-prefetch-request-put
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: prefetch-request-put
---
