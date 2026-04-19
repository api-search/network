---
class_count: 8
classes:
- Amount
- BalancePlatformNotificationResponse
- ResourceReference
- Resource
- TransactionNotificationRequestV4
- Transaction
- TransferData
- description
context_file: json-ld/adyen-transaction-webhooks-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-transaction-webhooks-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Transaction Webhooks from Adyen.
layout: jsonld
name: Adyen Transaction Webhooks Context
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
  name: currency
  type: string
- container: ''
  name: value
  type: integer
- container: ''
  name: notificationResponse
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: balancePlatform
  type: string
- container: ''
  name: creationDate
  type: dateTime
- container: ''
  name: data
  type: string
- container: ''
  name: environment
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: accountHolder
  type: string
- container: ''
  name: amount
  type: string
- container: ''
  name: balanceAccount
  type: string
- container: ''
  name: bookingDate
  type: dateTime
- container: ''
  name: status
  type: string
- container: ''
  name: transfer
  type: string
- container: ''
  name: valueDate
  type: dateTime
property_count: 17
provider_name: Adyen
provider_slug: adyen
slug: adyen-transaction-webhooks-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
