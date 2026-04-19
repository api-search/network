---
class_count: 2
classes:
- LoyaltyTransaction
- LoyaltyTransactionType
context_file: json-ld/adyen-terminal-loyalty-transaction-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-loyalty-transaction-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Loyalty Transaction from Adyen.
layout: jsonld
name: Adyen Terminal Loyalty Transaction Context
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
  name: Currency
  type: string
- container: ''
  name: TotalAmount
  type: decimal
- container: ''
  name: OriginalPOITransaction
  type: string
- container: ''
  name: TransactionConditions
  type: string
- container: set
  name: SaleItem
  type: string
property_count: 5
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-loyalty-transaction-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
