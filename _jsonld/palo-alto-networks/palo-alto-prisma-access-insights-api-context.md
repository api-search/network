---
class_count: 7
classes:
- CustomQuery
- DataResourceQuery
- DataResourceResponse
- ExportJobResponse
- ExportJobStatus
- QueryFilter
- TimeRange
context_file: json-ld/palo-alto-prisma-access-insights-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-prisma-access-insights-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Prisma Access Insights Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Prisma Access Insights Api Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: count
  type: integer
- container: set
  name: data
  type: reference
- container: ''
  name: downloadUrl
  type: reference
- container: ''
  name: enabledGranularity
  type: string
- container: ''
  name: errorMessage
  type: string
- container: ''
  name: expiresAt
  type: dateTime
- container: ''
  name: filter
  type: reference
- container: ''
  name: from
  type: dateTime
- container: set
  name: groupBy
  type: string
- container: ''
  name: header
  type: reference
- container: ''
  name: histogram
  type: reference
- container: ''
  name: jobId
  type: string
- container: ''
  name: last
  type: reference
- container: ''
  name: limit
  type: integer
- container: ''
  name: offset
  type: integer
- container: ''
  name: operator
  type: string
- container: ''
  name: order
  type: string
- container: ''
  name: pagination
  type: reference
- container: ''
  name: properties
  type: reference
- container: ''
  name: property
  type: string
- container: ''
  name: query
  type: reference
- container: ''
  name: requestId
  type: string
- container: ''
  name: resource
  type: string
- container: set
  name: rules
  type: reference
- container: ''
  name: sort
  type: reference
- container: ''
  name: status
  type: string
- container: ''
  name: submittedAt
  type: dateTime
- container: ''
  name: timeRange
  type: reference
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: to
  type: dateTime
- container: ''
  name: type
  type: string
- container: ''
  name: units
  type: string
- container: ''
  name: value
  type: reference
- container: set
  name: values
  type: string
property_count: 34
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-prisma-access-insights-api-context
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
- JSON-LD
- Linked Data
- Semantic Web
---
