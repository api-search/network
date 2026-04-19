---
class_count: 2
classes:
- MeApiCredential
- description
context_file: json-ld/adyen-management-me-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-me-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Me Api from Adyen.
layout: jsonld
name: Adyen Management Me Api Context
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
  name: Links
  type: string
- container: ''
  name: active
  type: boolean
- container: set
  name: allowedIpAddresses
  type: string
- container: set
  name: allowedOrigins
  type: string
- container: set
  name: associatedMerchantAccounts
  type: string
- container: ''
  name: clientKey
  type: string
- container: ''
  name: companyName
  type: string
- container: ''
  name: id
  type: string
- container: set
  name: roles
  type: string
- container: ''
  name: username
  type: string
property_count: 10
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-me-api-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
