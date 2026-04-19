---
description: Contains match target settings and a list of objects containing match targets with their assigned sequence number.
layout: schema
name: match-targets-sequence
properties_list:
- description: Contains the ID and sequence of a match target.
  name: targetSequence
  type: array
- description: Describes the type of match target, either `WEBSITE` or `API`.
  name: type
  type: string
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-match-targets-sequence-schema.json
slug: api-security-match-targets-sequence
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: match-targets-sequence
---
