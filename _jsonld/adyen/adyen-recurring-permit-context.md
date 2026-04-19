---
class_count: 1
classes:
- Permit
context_file: json-ld/adyen-recurring-permit-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-recurring-permit-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Recurring Permit from Adyen.
layout: jsonld
name: Adyen Recurring Permit Context
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
  name: partnerId
  type: string
- container: ''
  name: profileReference
  type: string
- container: ''
  name: restriction
  type: string
- container: ''
  name: resultKey
  type: string
- container: ''
  name: validTillDate
  type: dateTime
property_count: 5
provider_name: Adyen
provider_slug: adyen
slug: adyen-recurring-permit-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
