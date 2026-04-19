---
class_count: 1
classes:
- EventNotification
context_file: json-ld/adyen-terminal-event-notification-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-event-notification-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Event Notification from Adyen.
layout: jsonld
name: Adyen Terminal Event Notification Context
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
  name: TimeStamp
  type: dateTime
- container: ''
  name: EventToNotify
  type: string
- container: ''
  name: EventDetails
  type: string
- container: ''
  name: RejectedMessage
  type: string
- container: ''
  name: MaintenanceRequiredFlag
  type: boolean
- container: ''
  name: CustomerLanguage
  type: string
- container: set
  name: DisplayOutput
  type: string
property_count: 7
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-event-notification-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
