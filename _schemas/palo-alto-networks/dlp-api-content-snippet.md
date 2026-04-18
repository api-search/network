---
description: ContentSnippet schema from Palo Alto Networks Enterprise DLP API
layout: schema
name: ContentSnippet
properties_list:
- description: Data pattern identifier that matched.
  name: pattern_id
  type: string
- description: Data pattern name that matched.
  name: pattern_name
  type: string
- description: Context snippet around the data pattern match.
  name: snippet
  type: string
- description: Character offset position of the match within the document.
  name: position
  type: integer
- description: Whether the matched content within the snippet is masked.
  name: masked
  type: boolean
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/dlp-api-content-snippet-schema.json
slug: dlp-api-content-snippet
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ContentSnippet
---
