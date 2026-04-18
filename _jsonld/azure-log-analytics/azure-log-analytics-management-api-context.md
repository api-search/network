---
class_count: 5
classes:
- Workspace
- WorkspaceSku
- WorkspaceCapping
- SavedSearch
- Table
context_file: json-ld/azure-log-analytics-management-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/azure-log-analytics/refs/heads/main/json-ld/azure-log-analytics-management-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Azure Log Analytics Management Api from Azure Log Analytics.
layout: jsonld
name: Azure Log Analytics Management Api Context
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
  name: id
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: etag
  type: string
- container: ''
  name: customerId
  type: string
- container: ''
  name: provisioningState
  type: string
- container: ''
  name: retentionInDays
  type: integer
- container: ''
  name: publicNetworkAccessForIngestion
  type: string
- container: ''
  name: publicNetworkAccessForQuery
  type: string
- container: ''
  name: dailyQuotaGb
  type: double
- container: ''
  name: dataIngestionStatus
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: query
  type: string
- container: ''
  name: functionAlias
  type: string
- container: ''
  name: version
  type: integer
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: lastModifiedAt
  type: dateTime
property_count: 20
provider_name: Azure Log Analytics
provider_slug: azure-log-analytics
slug: azure-log-analytics-management-api-context
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
