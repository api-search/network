---
class_count: 3
classes:
- LogEntry
- DataCollectionRule
- StreamDeclaration
context_file: json-ld/azure-log-analytics-ingestion-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/azure-log-analytics/refs/heads/main/json-ld/azure-log-analytics-ingestion-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Azure Log Analytics Ingestion Api from Azure Log Analytics.
layout: jsonld
name: Azure Log Analytics Ingestion Api Context
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
  name: TimeGenerated
  type: dateTime
- container: ''
  name: Computer
  type: string
- container: ''
  name: AdditionalContext
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: kind
  type: string
- container: ''
  name: workspaceResourceId
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: transformKql
  type: string
- container: ''
  name: outputStream
  type: string
property_count: 10
provider_name: Azure Log Analytics
provider_slug: azure-log-analytics
slug: azure-log-analytics-ingestion-api-context
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
