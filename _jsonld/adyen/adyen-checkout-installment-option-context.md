---
class_count: 1
classes:
- InstallmentOption
context_file: json-ld/adyen-checkout-installment-option-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-installment-option-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Installment Option from Adyen.
layout: jsonld
name: Adyen Checkout Installment Option Context
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
  name: maxValue
  type: integer
- container: set
  name: plans
  type: string
- container: ''
  name: preselectedValue
  type: integer
- container: set
  name: values
  type: integer
property_count: 4
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-installment-option-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
