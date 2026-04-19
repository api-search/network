---
class_count: 1
classes:
- TransactionConditions
context_file: json-ld/adyen-terminal-transaction-conditions-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-transaction-conditions-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Transaction Conditions from Adyen.
layout: jsonld
name: Adyen Terminal Transaction Conditions Context
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
  name: AllowedPaymentBrand
  type: string
- container: set
  name: AcquirerID
  type: integer
- container: ''
  name: DebitPreferredFlag
  type: boolean
- container: set
  name: AllowedLoyaltyBrand
  type: string
- container: ''
  name: LoyaltyHandling
  type: string
- container: ''
  name: CustomerLanguage
  type: string
- container: ''
  name: ForceOnlineFlag
  type: boolean
- container: ''
  name: ForceEntryMode
  type: string
- container: ''
  name: MerchantCategoryCode
  type: string
property_count: 9
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-transaction-conditions-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
