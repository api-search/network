---
class_count: 5
classes:
- AllocationEntry
- AllocationRequest
- Entitlement
- Subscription
- SubscriptionEntitlements
context_file: json-ld/palo-alto-sase-subscription-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-sase-subscription-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Palo Alto Sase Subscription Api from Palo Alto Networks.
layout: jsonld
name: Palo Alto Sase Subscription Api Context
namespaces:
- prefix: pan
  uri: https://pan.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: allocatedQuantity
  type: integer
- container: set
  name: allocations
  type: reference
- container: ''
  name: availableQuantity
  type: integer
- container: ''
  name: endDate
  type: date
- container: set
  name: entitlements
  type: reference
- container: ''
  name: feature
  type: string
- container: ''
  name: licensedQuantity
  type: integer
- container: ''
  name: licensedUnit
  type: string
- container: ''
  name: productName
  type: string
- container: ''
  name: quantity
  type: integer
- container: ''
  name: sku
  type: string
- container: ''
  name: startDate
  type: date
- container: ''
  name: status
  type: string
- container: ''
  name: subscriptionId
  type: string
- container: ''
  name: supportLevel
  type: string
- container: ''
  name: tsgId
  type: string
- container: ''
  name: tsgName
  type: string
- container: ''
  name: unit
  type: string
- container: ''
  name: utilizedQuantity
  type: integer
property_count: 19
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: palo-alto-sase-subscription-api-context
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
- JSON-LD
- Linked Data
- Semantic Web
---
