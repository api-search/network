---
class_count: 3
classes:
- NotificationConfigurationDetails
- NotificationEventConfiguration
- description
context_file: json-ld/adyen-notification-configurations-notification-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-notification-configurations-notification-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Notification Configurations Notification from Adyen.
layout: jsonld
name: Adyen Notification Configurations Notification Context
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
  name: active
  type: boolean
- container: ''
  name: apiVersion
  type: integer
- container: set
  name: eventConfigs
  type: string
- container: ''
  name: hmacSignatureKey
  type: string
- container: ''
  name: notificationId
  type: integer
- container: ''
  name: notifyPassword
  type: string
- container: ''
  name: notifyURL
  type: string
- container: ''
  name: notifyUsername
  type: string
- container: ''
  name: sslProtocol
  type: string
- container: ''
  name: eventType
  type: string
- container: ''
  name: includeMode
  type: string
property_count: 11
provider_name: Adyen
provider_slug: adyen
slug: adyen-notification-configurations-notification-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
