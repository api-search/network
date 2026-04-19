---
description: Collects data needed for condition matches on Client Reputation.
layout: schema
name: client-reputation-condition
properties_list:
- description: The type of condition. In this case, `ClientReputationCondition`.
  name: className
  type: string
- description: Identifies the reputation category. Web scrapers (`WEBSCRP`) crawl sites and collect data like hotel rates, product prices, store locations, and more. DoS attackers (`DOSATCK`) are web clients or botn
  name: name
  type: array
- description: Whether the condition triggers on a match or lack of match.
  name: positiveMatch
  type: boolean
- description: Identifies the IP sharing. Either `NON_SHARED`, `SHARED_ONLY`, `BOTH`.
  name: sharedIpHandling
  type: string
- description: Threshold value that causes the trigger.
  name: value
  type: number
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-client-reputation-condition-schema.json
slug: api-security-client-reputation-condition
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: client-reputation-condition
---
