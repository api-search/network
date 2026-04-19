---
description: The settings for attack payload logging.
layout: schema
name: attack-payload-logging
properties_list:
- description: Use `ATTACK_PAYLOAD` to log attack payloads for all requests, or use `NONE` if you don't want to log the attack payloads. Note that when set to `NONE`, you'll see `redacted` in the logging information
  name: type
  type: string
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-attack-payload-logging-schema.json
slug: api-security-attack-payload-logging
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: attack-payload-logging
---
