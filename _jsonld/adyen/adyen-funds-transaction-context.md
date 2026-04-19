---
class_count: 2
classes:
- Transaction
- description
context_file: json-ld/adyen-funds-transaction-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-funds-transaction-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Funds Transaction from Adyen.
layout: jsonld
name: Adyen Funds Transaction Context
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
  name: amount
  type: string
- container: ''
  name: bankAccountDetail
  type: string
- container: ''
  name: captureMerchantReference
  type: string
- container: ''
  name: capturePspReference
  type: string
- container: ''
  name: creationDate
  type: dateTime
- container: ''
  name: destinationAccountCode
  type: string
- container: ''
  name: disputePspReference
  type: string
- container: ''
  name: disputeReasonCode
  type: string
- container: ''
  name: merchantReference
  type: string
- container: ''
  name: paymentPspReference
  type: string
- container: ''
  name: payoutPspReference
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: sourceAccountCode
  type: string
- container: ''
  name: transactionStatus
  type: string
- container: ''
  name: transferCode
  type: string
property_count: 15
provider_name: Adyen
provider_slug: adyen
slug: adyen-funds-transaction-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
