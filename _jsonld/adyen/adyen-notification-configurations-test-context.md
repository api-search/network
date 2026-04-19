---
class_count: 2
classes:
- TestNotificationConfigurationRequest
- TestNotificationConfigurationResponse
context_file: json-ld/adyen-notification-configurations-test-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-notification-configurations-test-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Notification Configurations Test from Adyen.
layout: jsonld
name: Adyen Notification Configurations Test Context
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
- container: set
  name: eventTypes
  type: string
- container: ''
  name: notificationId
  type: integer
- container: set
  name: errorMessages
  type: string
- container: set
  name: exchangeMessages
  type: string
- container: set
  name: invalidFields
  type: string
- container: set
  name: okMessages
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: resultCode
  type: string
property_count: 8
provider_name: Adyen
provider_slug: adyen
slug: adyen-notification-configurations-test-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
