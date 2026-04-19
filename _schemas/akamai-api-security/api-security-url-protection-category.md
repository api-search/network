---
description: Specify one or more load shedding categories for the URL protection policy.
layout: schema
name: url-protection-category
properties_list:
- description: Specify the type of traffic to shed first before reaching the requests per second (RPS) limit. `BOTS` includes bots from Akamai's existing list of known bots. `CLIENT_REPUTATIONS` includes traffic fro
  name: type
  type: string
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-url-protection-category-schema.json
slug: api-security-url-protection-category
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: url-protection-category
---
