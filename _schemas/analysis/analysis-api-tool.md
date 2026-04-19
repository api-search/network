---
description: Schema representing an API analysis, analytics, or monitoring tool
layout: schema
name: APIAnalysisTool
properties_list:
- description: Tool name
  name: name
  type: string
- description: Tool description
  name: description
  type: string
- description: Tool category
  name: category
  type: string
- description: License model
  name: license
  type: string
- description: Tool website URL
  name: url
  type: string
- description: GitHub repository URL
  name: github
  type: string
- description: Whether the tool exposes an API
  name: api
  type: boolean
- description: Classification tags
  name: tags
  type: array
provider_name: Analysis
provider_slug: analysis
schema_file: json-schema/analysis-api-tool-schema.json
slug: analysis-api-tool
tags:
- API Analysis
- API Governance
- API Linting
- API Monitoring
- API Security
- Analytics
- Observability
- Traffic Analysis
title: APIAnalysisTool
---
