---
class_count: 12
classes:
- StoredValueBalanceCheckRequest
- StoredValueBalanceCheckResponse
- StoredValueBalanceMergeRequest
- StoredValueBalanceMergeResponse
- StoredValueIssueRequest
- StoredValueIssueResponse
- StoredValueLoadRequest
- StoredValueLoadResponse
- StoredValueStatusChangeRequest
- StoredValueStatusChangeResponse
- StoredValueVoidRequest
- StoredValueVoidResponse
context_file: json-ld/adyen-stored-value-stored-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-stored-value-stored-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Stored Value Stored from Adyen.
layout: jsonld
name: Adyen Stored Value Stored Context
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
  name: merchantAccount
  type: string
- container: ''
  name: paymentMethod
  type: reference
- container: ''
  name: recurringDetailReference
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: shopperInteraction
  type: string
- container: ''
  name: shopperReference
  type: string
- container: ''
  name: store
  type: string
- container: ''
  name: currentBalance
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: refusalReason
  type: string
- container: ''
  name: resultCode
  type: string
- container: ''
  name: thirdPartyRefusalReason
  type: string
- container: ''
  name: sourcePaymentMethod
  type: reference
- container: ''
  name: authCode
  type: string
- container: ''
  name: loadType
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: originalReference
  type: string
- container: ''
  name: tenderReference
  type: string
- container: ''
  name: uniqueTerminalId
  type: string
property_count: 20
provider_name: Adyen
provider_slug: adyen
slug: adyen-stored-value-stored-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
