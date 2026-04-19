---
class_count: 8
classes:
- StoredValueAccountID
- StoredValueAccountStatus
- StoredValueAccountType
- StoredValueData
- StoredValueRequest
- StoredValueResponse
- StoredValueResult
- StoredValueTransactionType
context_file: json-ld/adyen-terminal-stored-value-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-stored-value-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Stored Value from Adyen.
layout: jsonld
name: Adyen Terminal Stored Value Context
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
  name: StoredValueProvider
  type: string
- container: ''
  name: OwnerName
  type: string
- container: ''
  name: ExpiryDate
  type: integer
- container: ''
  name: EntryMode
  type: string
- container: ''
  name: IdentificationType
  type: string
- container: ''
  name: StoredValueID
  type: string
- container: ''
  name: CurrentBalance
  type: decimal
- container: ''
  name: OriginalPOITransaction
  type: string
- container: ''
  name: ProductCode
  type: integer
- container: ''
  name: EanUpc
  type: integer
- container: ''
  name: ItemAmount
  type: decimal
- container: ''
  name: Currency
  type: string
- container: ''
  name: SaleData
  type: string
- container: ''
  name: CustomerLanguage
  type: string
- container: ''
  name: Response
  type: string
- container: ''
  name: POIData
  type: string
- container: set
  name: PaymentReceipt
  type: string
- container: ''
  name: HostTransactionID
  type: string
property_count: 18
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-stored-value-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
