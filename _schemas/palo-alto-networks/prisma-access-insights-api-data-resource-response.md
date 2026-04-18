---
description: Response containing data resource query results
layout: schema
name: DataResourceResponse
properties_list:
- description: Response metadata
  name: header
  type: object
- description: Array of result records
  name: data
  type: array
- description: Total number of records matching the query
  name: count
  type: integer
- description: Pagination information
  name: pagination
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-insights-api-data-resource-response-schema.json
slug: prisma-access-insights-api-data-resource-response
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: DataResourceResponse
---
