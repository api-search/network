---
class_count: 10
classes:
- Account
- Contact
- Invoice
- Payment
- JournalEntry
- Expense
- CompanyInfo
- Item
- TaxRate
- PurchaseOrder
context_file: json-ld/merge-accounting-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/json-ld/merge-accounting-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Merge Accounting Api from Merge.
layout: jsonld
name: Merge Accounting Api Context
namespaces:
- prefix: merge
  uri: https://api.merge.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: classification
  type: string
- container: ''
  name: currentBalance
  type: decimal
- container: ''
  name: currency
  type: string
- container: ''
  name: accountNumber
  type: string
- container: ''
  name: isSupplier
  type: boolean
- container: ''
  name: isCustomer
  type: boolean
- container: ''
  name: emailAddress
  type: string
- container: ''
  name: number
  type: string
- container: ''
  name: issueDate
  type: dateTime
- container: ''
  name: dueDate
  type: dateTime
- container: ''
  name: totalAmount
  type: decimal
- container: ''
  name: balance
  type: decimal
- container: ''
  name: status
  type: string
- container: ''
  name: transactionDate
  type: dateTime
- container: ''
  name: memo
  type: string
- container: ''
  name: legalName
  type: string
- container: ''
  name: unitPrice
  type: decimal
- container: ''
  name: totalTaxRate
  type: decimal
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: modifiedAt
  type: dateTime
- container: ''
  name: remoteWasDeleted
  type: boolean
property_count: 24
provider_name: Merge
provider_slug: merge
slug: merge-accounting-api-context
tags:
- Integrations
- Platform
- Unified API
- JSON-LD
- Linked Data
- Semantic Web
---
