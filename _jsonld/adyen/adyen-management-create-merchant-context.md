---
class_count: 8
classes:
- CreateMerchantRequest
- CreateMerchantResponse
- CreateMerchantUserRequest
- CreateMerchantWebhookRequest
- description
- email
- name
- url
context_file: json-ld/adyen-management-create-merchant-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-create-merchant-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Create Merchant from Adyen.
layout: jsonld
name: Adyen Management Create Merchant Context
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
  name: businessLineId
  type: string
- container: ''
  name: companyId
  type: string
- container: ''
  name: legalEntityId
  type: string
- container: ''
  name: pricingPlan
  type: string
- container: ''
  name: reference
  type: string
- container: set
  name: salesChannels
  type: string
- container: ''
  name: id
  type: string
- container: set
  name: accountGroups
  type: string
- container: set
  name: roles
  type: string
- container: ''
  name: timeZoneCode
  type: string
- container: ''
  name: username
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
  name: active
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
  name: type
  type: string
property_count: 22
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-create-merchant-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
