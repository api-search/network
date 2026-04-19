---
class_count: 3
classes:
- CostEstimateAssumptions
- CostEstimateRequest
- CostEstimateResponse
context_file: json-ld/adyen-binlookup-cost-estimate-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-binlookup-cost-estimate-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Binlookup Cost Estimate from Adyen.
layout: jsonld
name: Adyen Binlookup Cost Estimate Context
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
  name: assume3DSecureAuthenticated
  type: boolean
- container: ''
  name: assumeLevel3Data
  type: boolean
- container: ''
  name: installments
  type: integer
- container: ''
  name: amount
  type: string
- container: ''
  name: assumptions
  type: string
- container: ''
  name: cardNumber
  type: string
- container: ''
  name: encryptedCardNumber
  type: string
- container: ''
  name: merchantAccount
  type: string
- container: ''
  name: merchantDetails
  type: string
- container: ''
  name: recurring
  type: string
- container: ''
  name: selectedRecurringDetailReference
  type: string
- container: ''
  name: shopperInteraction
  type: string
- container: ''
  name: shopperReference
  type: string
- container: ''
  name: cardBin
  type: string
- container: ''
  name: costEstimateAmount
  type: string
- container: ''
  name: costEstimateReference
  type: string
- container: ''
  name: resultCode
  type: string
- container: ''
  name: surchargeType
  type: string
property_count: 18
provider_name: Adyen
provider_slug: adyen
slug: adyen-binlookup-cost-estimate-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
