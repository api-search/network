---
description: ''
layout: schema
name: SearchResults
properties_list:
- description: Starting offset of results
  name: init_offset
  type: integer
- description: Array of result rows
  name: results
  type: array
- description: Metadata about the fields in the results
  name: fields
  type: array
- description: ''
  name: messages
  type: array
- description: Whether results are preview (partial) results
  name: preview
  type: boolean
- description: Highlighted terms in results
  name: highlighted
  type: object
provider_name: Splunk
provider_slug: splunk
schema_file: json-schema/splunk-enterprise-rest-search-results-schema.json
slug: splunk-enterprise-rest-search-results
tags:
- Analytics
- Data Analysis
- Logging
- Machine Data
- Monitoring
- Observability
- Platform
- Security
- SIEM
title: SearchResults
---
