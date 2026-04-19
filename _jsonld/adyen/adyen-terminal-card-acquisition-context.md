---
class_count: 3
classes:
- CardAcquisitionRequest
- CardAcquisitionResponse
- CardAcquisitionTransaction
context_file: json-ld/adyen-terminal-card-acquisition-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-card-acquisition-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Card Acquisition from Adyen.
layout: jsonld
name: Adyen Terminal Card Acquisition Context
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
  name: SaleData
  type: string
- container: ''
  name: Response
  type: string
- container: ''
  name: POIData
  type: string
- container: ''
  name: CustomerLanguage
  type: string
- container: set
  name: PaymentBrand
  type: string
- container: ''
  name: PaymentInstrumentData
  type: string
- container: set
  name: LoyaltyAccount
  type: string
- container: set
  name: AllowedPaymentBrand
  type: string
- container: set
  name: AllowedLoyaltyBrand
  type: string
- container: ''
  name: LoyaltyHandling
  type: string
- container: ''
  name: ForceEntryMode
  type: string
- container: ''
  name: ForceCustomerSelectionFlag
  type: boolean
- container: ''
  name: TotalAmount
  type: decimal
- container: ''
  name: PaymentType
  type: string
- container: ''
  name: CashBackFlag
  type: boolean
property_count: 15
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-card-acquisition-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
