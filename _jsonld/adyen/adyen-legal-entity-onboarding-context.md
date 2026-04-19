---
class_count: 6
classes:
- OnboardingLinkInfo
- OnboardingLink
- OnboardingTheme
- OnboardingThemes
- url
- description
context_file: json-ld/adyen-legal-entity-onboarding-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-legal-entity-onboarding-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Legal Entity Onboarding from Adyen.
layout: jsonld
name: Adyen Legal Entity Onboarding Context
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
  name: locale
  type: string
- container: ''
  name: redirectUrl
  type: string
- container: ''
  name: settings
  type: reference
- container: ''
  name: themeId
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: id
  type: string
- container: ''
  name: properties
  type: reference
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: next
  type: string
- container: ''
  name: previous
  type: string
- container: set
  name: themes
  type: string
property_count: 11
provider_name: Adyen
provider_slug: adyen
slug: adyen-legal-entity-onboarding-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
