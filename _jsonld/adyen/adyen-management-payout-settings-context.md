---
class_count: 3
classes:
- PayoutSettingsRequest
- PayoutSettingsResponse
- PayoutSettings
context_file: json-ld/adyen-management-payout-settings-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-payout-settings-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Payout Settings from Adyen.
layout: jsonld
name: Adyen Management Payout Settings Context
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
  name: enabled
  type: boolean
- container: ''
  name: enabledFromDate
  type: string
- container: ''
  name: transferInstrumentId
  type: string
- container: set
  name: data
  type: string
- container: ''
  name: allowed
  type: boolean
- container: ''
  name: id
  type: string
- container: ''
  name: priority
  type: string
- container: ''
  name: verificationStatus
  type: string
property_count: 8
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-payout-settings-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
