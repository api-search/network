---
description: A filter criterion for querying XDR resources.
layout: schema
name: Filter
properties_list:
- description: Field name to filter on (e.g., incident_id, status, severity).
  name: field
  type: string
- description: Comparison operator.
  name: operator
  type: string
- description: Filter value. Use an array for the "in" operator, a string or integer for others.
  name: value
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xdr-api-filter-schema.json
slug: cortex-xdr-api-filter
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
