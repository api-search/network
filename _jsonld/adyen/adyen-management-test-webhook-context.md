---
class_count: 2
classes:
- TestWebhookRequest
- TestWebhookResponse
context_file: json-ld/adyen-management-test-webhook-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-test-webhook-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Test Webhook from Adyen.
layout: jsonld
name: Adyen Management Test Webhook Context
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
  name: notification
  type: string
- container: set
  name: types
  type: string
- container: set
  name: data
  type: string
property_count: 3
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-test-webhook-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
