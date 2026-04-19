---
class_count: 1
classes:
- Instalment
context_file: json-ld/adyen-terminal-instalment-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-terminal-instalment-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Terminal Instalment from Adyen.
layout: jsonld
name: Adyen Terminal Instalment Context
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
  name: InstalmentType
  type: string
- container: ''
  name: SequenceNumber
  type: integer
- container: ''
  name: PlanID
  type: string
- container: ''
  name: Period
  type: integer
- container: ''
  name: PeriodUnit
  type: string
- container: ''
  name: FirstPaymentDate
  type: date
- container: ''
  name: TotalNbOfPayments
  type: integer
- container: ''
  name: CumulativeAmount
  type: decimal
- container: ''
  name: FirstAmount
  type: decimal
- container: ''
  name: Charges
  type: decimal
property_count: 10
provider_name: Adyen
provider_slug: adyen
slug: adyen-terminal-instalment-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
