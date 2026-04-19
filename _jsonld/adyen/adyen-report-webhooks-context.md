---
class_count: 6
classes:
- BalancePlatformNotificationResponse
- ReportNotificationData
- ReportNotificationRequest
- ResourceReference
- Resource
- description
context_file: json-ld/adyen-report-webhooks-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-report-webhooks-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Report Webhooks from Adyen.
layout: jsonld
name: Adyen Report Webhooks Context
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
  name: notificationResponse
  type: string
- container: ''
  name: accountHolder
  type: string
- container: ''
  name: balanceAccount
  type: string
- container: ''
  name: balancePlatform
  type: string
- container: ''
  name: creationDate
  type: dateTime
- container: ''
  name: downloadUrl
  type: string
- container: ''
  name: fileName
  type: string
- container: ''
  name: reportType
  type: string
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
  name: id
  type: string
- container: ''
  name: reference
  type: string
property_count: 13
provider_name: Adyen
provider_slug: adyen
slug: adyen-report-webhooks-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
