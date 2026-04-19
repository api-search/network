---
class_count: 18
classes:
- CustomerList
- Subscription
- SubscriptionList
- Product
- description
- InvoiceList
- Pagination
- InvoiceLineItem
- CustomerRequest
- email
- SubscriptionRequest
- Address
- Customer
- createdAt
- updatedAt
- CustomerUpdate
- Invoice
- ProductList
context_file: json-ld/amdocs-connectx-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amdocs/refs/heads/main/json-ld/amdocs-connectx-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amdocs Connectx from Amdocs.
layout: jsonld
name: Amdocs Connectx Context
namespaces:
- prefix: amdocs
  uri: https://amdocs.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: data
  type: string
- container: ''
  name: pagination
  type: string
- container: ''
  name: subscriptionId
  type: string
- container: ''
  name: customerId
  type: string
- container: ''
  name: productId
  type: string
- container: ''
  name: productName
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: startDate
  type: date
- container: ''
  name: endDate
  type: date
- container: ''
  name: monthlyCharge
  type: decimal
- container: ''
  name: currency
  type: string
- container: set
  name: addons
  type: string
- container: ''
  name: productType
  type: string
- container: ''
  name: monthlyPrice
  type: decimal
- container: set
  name: features
  type: string
- container: ''
  name: page
  type: integer
- container: ''
  name: pageSize
  type: integer
- container: ''
  name: totalPages
  type: integer
- container: ''
  name: totalItems
  type: integer
- container: ''
  name: quantity
  type: decimal
- container: ''
  name: unitPrice
  type: decimal
- container: ''
  name: amount
  type: decimal
- container: ''
  name: customerType
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: companyName
  type: string
- container: ''
  name: phone
  type: string
- container: ''
  name: address
  type: string
- container: ''
  name: street
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: postalCode
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: accountNumber
  type: string
- container: ''
  name: billingAddress
  type: string
- container: ''
  name: invoiceId
  type: string
- container: ''
  name: invoiceNumber
  type: string
- container: ''
  name: invoiceDate
  type: date
- container: ''
  name: dueDate
  type: date
- container: ''
  name: totalAmount
  type: decimal
- container: ''
  name: taxAmount
  type: decimal
- container: set
  name: lineItems
  type: string
property_count: 42
provider_name: Amdocs
provider_slug: amdocs
slug: amdocs-connectx-context
tags:
- Telecom
- BSS
- OSS
- Billing
- Customer Management
- MVNO
- 5G
- SaaS
- JSON-LD
- Linked Data
- Semantic Web
---
