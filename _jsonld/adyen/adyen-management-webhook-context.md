---
class_count: 3
classes:
- Webhook
- description
- url
context_file: json-ld/adyen-management-webhook-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-webhook-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Webhook from Adyen.
layout: jsonld
name: Adyen Management Webhook Context
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
  name: acceptsExpiredCertificate
  type: boolean
- container: ''
  name: acceptsSelfSignedCertificate
  type: boolean
- container: ''
  name: acceptsUntrustedRootCertificate
  type: boolean
- container: ''
  name: accountReference
  type: string
- container: ''
  name: active
  type: boolean
- container: ''
  name: additionalSettings
  type: string
- container: ''
  name: certificateAlias
  type: string
- container: ''
  name: communicationFormat
  type: string
- container: ''
  name: encryptionProtocol
  type: string
- container: ''
  name: filterMerchantAccountType
  type: string
- container: set
  name: filterMerchantAccounts
  type: string
- container: ''
  name: hasError
  type: boolean
- container: ''
  name: hasPassword
  type: boolean
- container: ''
  name: hmacKeyCheckValue
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: networkType
  type: string
- container: ''
  name: populateSoapActionHeader
  type: boolean
- container: ''
  name: type
  type: string
- container: ''
  name: username
  type: string
property_count: 20
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-webhook-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
