---
description: Contains details about a reputation profile.
layout: schema
name: reputation-profile
properties_list:
- description: Contains information about the criteria that trigger the reputation profile.
  name: condition
  type: object
- description: Identifies the reputation category. Web scrapers (`WEBSCRP`) crawl sites and collect data like hotel rates, product prices, store locations, and more. DoS attackers (`DOSATCK`) are web clients or botn
  name: context
  type: string
- description: __Read-only__ Describes the reputation category.
  name: contextReadable
  type: string
- description: Describes the reputation profile.
  name: description
  type: string
- description: __Read-only__ Whether you enabled the reputation profile.
  name: enabled
  type: boolean
- description: __Read-only__ Uniquely identifies the reputation profile.
  name: id
  type: integer
- description: The name you assigned to the reputation profile.
  name: name
  type: string
- description: Identifies the IP sharing. Either `NON_SHARED`, `SHARED_ONLY`, `BOTH`.
  name: sharedIpHandling
  type: string
- description: The threshold when the profile to triggers.
  name: threshold
  type: number
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-reputation-profile-schema.json
slug: api-security-reputation-profile
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: reputation-profile
---
