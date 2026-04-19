---
class_count: 5
classes:
- BalanceAccountBase
- BalanceAccountInfo
- BalanceAccount
- BalanceAccountUpdateRequest
- description
context_file: json-ld/adyen-configuration-balance-account-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-configuration-balance-account-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Configuration Balance Account from Adyen.
layout: jsonld
name: Adyen Configuration Balance Account Context
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
  name: accountHolderId
  type: string
- container: ''
  name: defaultCurrencyCode
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: metadata
  type: reference
- container: ''
  name: migratedAccountCode
  type: string
- container: ''
  name: platformPaymentConfiguration
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: timeZone
  type: string
- container: set
  name: balances
  type: string
property_count: 10
provider_name: Adyen
provider_slug: adyen
slug: adyen-configuration-balance-account-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
