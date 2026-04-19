---
description: The GET Response JSON for attack payload logging.
layout: schema
name: attack-payload-logging-get-200
properties_list:
- description: Whether attack payload logging is enabled.
  name: enabled
  type: boolean
- description: The settings for how Akamai's network logs attack payloads in request bodies.
  name: requestBody
  type: object
- description: The settings for how Akamai's network logs attack payloads in response bodies.
  name: responseBody
  type: object
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-attack-payload-logging-get-200-schema.json
slug: api-security-attack-payload-logging-get-200
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: attack-payload-logging-get-200
---
