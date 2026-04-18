---
description: A filter criterion for querying XSIAM resources.
layout: schema
name: Filter
properties_list:
- description: Field name to filter on.
  name: field
  type: string
- description: ''
  name: operator
  type: string
- description: Filter value (string, integer, or array for the "in" operator).
  name: value
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsiam-api-filter-schema.json
slug: cortex-xsiam-api-filter
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Filter
---
