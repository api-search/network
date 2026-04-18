---
class_count: 6
classes:
- QueryBody
- QueryResults
- Table
- Column
- ErrorResponse
- ErrorDetail
context_file: json-ld/azure-log-analytics-query-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/azure-log-analytics/refs/heads/main/json-ld/azure-log-analytics-query-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Azure Log Analytics Query Api from Azure Log Analytics.
layout: jsonld
name: Azure Log Analytics Query Api Context
namespaces:
- prefix: azure
  uri: https://learn.microsoft.com/en-us/azure/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: query
  type: string
- container: ''
  name: timespan
  type: string
- container: set
  name: workspaces
  type: string
- container: set
  name: tables
  type: reference
- container: ''
  name: name
  type: string
- container: set
  name: columns
  type: reference
- container: set
  name: rows
  type: ''
- container: ''
  name: type
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: message
  type: string
- container: set
  name: details
  type: reference
property_count: 11
provider_name: Azure Log Analytics
provider_slug: azure-log-analytics
slug: azure-log-analytics-query-api-context
tags:
- Analytics
- Azure
- Cloud
- Logging
- Monitoring
- JSON-LD
- Linked Data
- Semantic Web
---
