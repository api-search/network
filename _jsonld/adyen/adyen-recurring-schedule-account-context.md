---
class_count: 2
classes:
- ScheduleAccountUpdaterRequest
- ScheduleAccountUpdaterResult
context_file: json-ld/adyen-recurring-schedule-account-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-recurring-schedule-account-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Recurring Schedule Account from Adyen.
layout: jsonld
name: Adyen Recurring Schedule Account Context
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
  name: additionalData
  type: reference
- container: ''
  name: card
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: selectedRecurringDetailReference
  type: string
- container: ''
  name: shopperReference
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: result
  type: string
property_count: 8
provider_name: Adyen
provider_slug: adyen
slug: adyen-recurring-schedule-account-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
