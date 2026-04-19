---
class_count: 8
classes:
- Amount
- AuthenticationInfo
- AuthenticationNotificationData
- AuthenticationNotificationRequest
- BalancePlatformNotificationResponse
- ChallengeInfo
- PurchaseInfo
- Resource
context_file: json-ld/adyen-authentication-webhooks-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-authentication-webhooks-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Authentication Webhooks from Adyen.
layout: jsonld
name: Adyen Authentication Webhooks Context
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
  name: acsTransId
  type: string
- container: ''
  name: challenge
  type: string
- container: ''
  name: challengeIndicator
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: deviceChannel
  type: string
- container: ''
  name: dsTransID
  type: string
- container: ''
  name: exemptionIndicator
  type: string
- container: ''
  name: inPSD2Scope
  type: boolean
- container: ''
  name: messageCategory
  type: string
- container: ''
  name: messageVersion
  type: string
- container: ''
  name: riskScore
  type: integer
- container: ''
  name: threeDSServerTransID
  type: string
- container: ''
  name: transStatus
  type: string
- container: ''
  name: transStatusReason
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: authentication
  type: string
- container: ''
  name: balancePlatform
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: paymentInstrumentId
  type: string
- container: ''
  name: purchase
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: data
  type: string
- container: ''
  name: environment
  type: string
- container: ''
  name: notificationResponse
  type: string
- container: ''
  name: challengeCancel
  type: string
- container: ''
  name: flow
  type: string
- container: ''
  name: lastInteraction
  type: dateTime
- container: ''
  name: phoneNumber
  type: string
- container: ''
  name: resends
  type: integer
- container: ''
  name: retries
  type: integer
- container: ''
  name: date
  type: string
- container: ''
  name: merchantName
  type: string
- container: ''
  name: originalAmount
  type: string
- container: ''
  name: creationDate
  type: dateTime
property_count: 36
provider_name: Adyen
provider_slug: adyen
slug: adyen-authentication-webhooks-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
