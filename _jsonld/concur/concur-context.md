---
class_count: 2
classes:
- ExpenseReport
- Expense
context_file: json-ld/concur-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/concur/refs/heads/main/json-ld/concur-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Concur from SAP Concur.
layout: jsonld
name: Concur Context
namespaces:
- prefix: concur
  uri: https://concur.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: reportId
  type: string
- container: ''
  name: reportName
  type: string
- container: ''
  name: ownerName
  type: string
- container: ''
  name: businessPurpose
  type: string
- container: ''
  name: submitDate
  type: dateTime
- container: ''
  name: approvalStatus
  type: string
- container: ''
  name: total
  type: decimal
- container: ''
  name: currencyCode
  type: string
- container: ''
  name: expenseId
  type: string
- container: ''
  name: expenseTypeName
  type: string
- container: ''
  name: transactionDate
  type: date
- container: ''
  name: transactionAmount
  type: decimal
- container: ''
  name: vendorName
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: receiptRequired
  type: boolean
property_count: 15
provider_name: SAP Concur
provider_slug: concur
slug: concur-context
tags:
- Expense Management
- Finance
- Invoice
- SAP
- Travel
- JSON-LD
- Linked Data
- Semantic Web
---
