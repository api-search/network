---
class_count: 6
classes:
- UpdateMerchantUserRequest
- UpdateMerchantWebhookRequest
- email
- name
- description
- url
context_file: json-ld/adyen-management-update-merchant-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-update-merchant-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Update Merchant from Adyen.
layout: jsonld
name: Adyen Management Update Merchant Context
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
- container: set
  name: accountGroups
  type: string
- container: ''
  name: active
  type: boolean
- container: set
  name: roles
  type: string
- container: ''
  name: timeZoneCode
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
  name: additionalSettings
  type: string
- container: ''
  name: communicationFormat
  type: string
- container: ''
  name: encryptionProtocol
  type: string
- container: ''
  name: networkType
  type: string
- container: ''
  name: password
  type: string
- container: ''
  name: populateSoapActionHeader
  type: boolean
- container: ''
  name: username
  type: string
property_count: 14
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-update-merchant-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
