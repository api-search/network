---
description: Defines a `CLIENT_LIST` load shedding category for a URL protection policy.
layout: schema
name: url-protection-client-list-category
properties_list:
- description: A list of client list identifiers to match on.
  name: listIds
  type: array
- description: Whether the selected client lists match.
  name: positiveMatch
  type: boolean
- description: Specify `CLIENT_LIST` to match on a client list.
  name: type
  type: string
provider_name: Akamai API Security
provider_slug: akamai-api-security
schema_file: json-schema/api-security-url-protection-client-list-category-schema.json
slug: api-security-url-protection-client-list-category
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
title: url-protection-client-list-category
---
