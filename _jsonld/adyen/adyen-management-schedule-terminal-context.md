---
class_count: 2
classes:
- ScheduleTerminalActionsRequest
- ScheduleTerminalActionsResponse
context_file: json-ld/adyen-management-schedule-terminal-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-schedule-terminal-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Schedule Terminal from Adyen.
layout: jsonld
name: Adyen Management Schedule Terminal Context
namespaces:
- prefix: adyen
  uri: https://docs.adyen.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: actionDetails
  type: string
- container: ''
  name: scheduledAt
  type: string
- container: ''
  name: storeId
  type: string
- container: set
  name: terminalIds
  type: string
- container: set
  name: items
  type: string
- container: ''
  name: terminalsWithErrors
  type: reference
- container: ''
  name: totalErrors
  type: integer
- container: ''
  name: totalScheduled
  type: integer
property_count: 8
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-schedule-terminal-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
