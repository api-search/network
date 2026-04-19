---
class_count: 1
classes:
- CapabilitySettings
context_file: json-ld/adyen-configuration-capability-settings-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-configuration-capability-settings-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Configuration Capability Settings from Adyen.
layout: jsonld
name: Adyen Configuration Capability Settings Context
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
  name: amountPerIndustry
  type: reference
- container: ''
  name: authorizedCardUsers
  type: boolean
- container: set
  name: fundingSource
  type: string
- container: ''
  name: interval
  type: string
- container: ''
  name: maxAmount
  type: string
property_count: 5
provider_name: Adyen
provider_slug: adyen
slug: adyen-configuration-capability-settings-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
