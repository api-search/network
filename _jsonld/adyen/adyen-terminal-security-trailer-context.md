---
class_count: 1
classes:
- SecurityTrailer
context_file: json-ld/adyen-terminal-security-trailer-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-security-trailer-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Security Trailer from Adyen.
layout: jsonld
name: Adyen Terminal Security Trailer Context
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
  name: AdyenCryptoVersion
  type: integer
- container: ''
  name: KeyIdentifier
  type: string
- container: ''
  name: KeyVersion
  type: integer
- container: ''
  name: Nonce
  type: string
- container: ''
  name: Hmac
  type: string
property_count: 5
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-security-trailer-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
