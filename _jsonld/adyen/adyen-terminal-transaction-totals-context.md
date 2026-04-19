---
class_count: 1
classes:
- TransactionTotals
context_file: json-ld/adyen-terminal-transaction-totals-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-transaction-totals-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Transaction Totals from Adyen.
layout: jsonld
name: Adyen Terminal Transaction Totals Context
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
  name: PaymentInstrumentType
  type: string
- container: ''
  name: AcquirerID
  type: integer
- container: ''
  name: HostReconciliationID
  type: string
- container: ''
  name: CardBrand
  type: string
- container: ''
  name: POIID
  type: string
- container: ''
  name: SaleID
  type: string
- container: ''
  name: OperatorID
  type: string
- container: ''
  name: ShiftNumber
  type: string
- container: ''
  name: TotalsGroupID
  type: string
- container: ''
  name: PaymentCurrency
  type: string
- container: set
  name: PaymentTotals
  type: string
- container: ''
  name: LoyaltyUnit
  type: string
- container: ''
  name: LoyaltyCurrency
  type: string
- container: set
  name: LoyaltyTotals
  type: string
property_count: 14
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-transaction-totals-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
