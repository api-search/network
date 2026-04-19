---
class_count: 1
classes:
- MobileData
context_file: json-ld/adyen-terminal-mobile-data-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-mobile-data-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Mobile Data from Adyen.
layout: jsonld
name: Adyen Terminal Mobile Data Context
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
  name: MobileCountryCode
  type: integer
- container: ''
  name: MobileNetworkCode
  type: integer
- container: ''
  name: MaskedMSISDN
  type: integer
- container: ''
  name: Geolocation
  type: string
- container: ''
  name: ProtectedMobileData
  type: string
- container: ''
  name: SensitiveMobileData
  type: string
property_count: 6
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-mobile-data-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
