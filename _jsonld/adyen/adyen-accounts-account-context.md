---
class_count: 2
classes:
- Account
- description
context_file: json-ld/adyen-accounts-account-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-accounts-account-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Accounts Account from Adyen.
layout: jsonld
name: Adyen Accounts Account Context
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
  name: accountCode
  type: string
- container: ''
  name: bankAccountUUID
  type: string
- container: ''
  name: beneficiaryAccount
  type: string
- container: ''
  name: beneficiaryMerchantReference
  type: string
- container: ''
  name: metadata
  type: reference
- container: ''
  name: payoutMethodCode
  type: string
- container: ''
  name: payoutSchedule
  type: string
- container: ''
  name: payoutSpeed
  type: string
- container: ''
  name: status
  type: string
property_count: 9
provider_name: Adyen
provider_slug: adyen
slug: adyen-accounts-account-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
