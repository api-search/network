---
class_count: 6
classes:
- PromoConfig
- FinancingTerm
- PromoResponse
- PromoContent
- description
- OfferContent
context_file: json-ld/affirm-promos-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/affirm/refs/heads/main/json-ld/affirm-promos-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Affirm Promos from affirm.
layout: jsonld
name: Affirm Promos Context
namespaces:
- prefix: affirm
  uri: https://affirm.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: promoPrequalEnabled
  type: boolean
- container: ''
  name: merchantName
  type: string
- container: ''
  name: merchantAri
  type: string
- container: ''
  name: userAri
  type: string
- container: ''
  name: toastEnabled
  type: boolean
- container: set
  name: enabledIntegrations
  type: string
- container: ''
  name: images
  type: reference
- container: ''
  name: hero
  type: reference
- container: ''
  name: hero2x
  type: reference
- container: ''
  name: logo
  type: reference
- container: ''
  name: logo2x
  type: reference
- container: ''
  name: amount
  type: integer
- container: ''
  name: loanType
  type: string
- container: ''
  name: apr
  type: decimal
- container: ''
  name: installmentAmount
  type: integer
- container: ''
  name: installmentCount
  type: integer
- container: ''
  name: interestAmount
  type: integer
- container: ''
  name: totalAmount
  type: integer
- container: ''
  name: promo
  type: string
- container: ''
  name: offer
  type: string
- container: ''
  name: ala
  type: string
- container: ''
  name: htmlAla
  type: string
- container: ''
  name: headline
  type: string
- container: ''
  name: tagline
  type: string
- container: ''
  name: button
  type: string
- container: ''
  name: htmlFooter
  type: string
- container: ''
  name: config
  type: string
- container: ''
  name: minimumLoanAmount
  type: decimal
- container: ''
  name: maximumLoanAmount
  type: decimal
- container: set
  name: terms
  type: string
property_count: 30
provider_name: affirm
provider_slug: affirm
slug: affirm-promos-context
tags:
- JSON-LD
- Linked Data
- Semantic Web
---
