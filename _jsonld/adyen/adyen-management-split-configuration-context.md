---
class_count: 5
classes:
- SplitConfigurationList
- SplitConfigurationLogic
- SplitConfigurationRule
- SplitConfiguration
- description
context_file: json-ld/adyen-management-split-configuration-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-split-configuration-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Split Configuration from Adyen.
layout: jsonld
name: Adyen Management Split Configuration Context
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
  name: data
  type: string
- container: ''
  name: acquiringFees
  type: string
- container: ''
  name: additionalCommission
  type: string
- container: ''
  name: adyenCommission
  type: string
- container: ''
  name: adyenFees
  type: string
- container: ''
  name: adyenMarkup
  type: string
- container: ''
  name: chargeback
  type: string
- container: ''
  name: chargebackCostAllocation
  type: string
- container: ''
  name: commission
  type: string
- container: ''
  name: interchange
  type: string
- container: ''
  name: paymentFee
  type: string
- container: ''
  name: remainder
  type: string
- container: ''
  name: schemeFee
  type: string
- container: ''
  name: splitLogicId
  type: string
- container: ''
  name: surcharge
  type: string
- container: ''
  name: tip
  type: string
- container: ''
  name: currency
  type: string
- container: ''
  name: fundingSource
  type: string
- container: ''
  name: paymentMethod
  type: string
- container: ''
  name: ruleId
  type: string
- container: ''
  name: shopperInteraction
  type: string
- container: ''
  name: splitLogic
  type: string
- container: set
  name: rules
  type: string
- container: ''
  name: splitConfigurationId
  type: string
- container: set
  name: stores
  type: string
property_count: 25
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-split-configuration-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
