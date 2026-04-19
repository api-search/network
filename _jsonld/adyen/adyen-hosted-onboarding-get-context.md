---
class_count: 4
classes:
- GetOnboardingUrlRequest
- GetOnboardingUrlResponse
- GetPciUrlRequest
- GetPciUrlResponse
context_file: json-ld/adyen-hosted-onboarding-get-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-hosted-onboarding-get-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Hosted Onboarding Get from Adyen.
layout: jsonld
name: Adyen Hosted Onboarding Get Context
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
  name: accountHolderCode
  type: string
- container: ''
  name: collectInformation
  type: string
- container: ''
  name: editMode
  type: boolean
- container: ''
  name: mobileOAuthCallbackUrl
  type: string
- container: ''
  name: platformName
  type: string
- container: ''
  name: returnUrl
  type: string
- container: ''
  name: shopperLocale
  type: string
- container: ''
  name: showPages
  type: string
- container: set
  name: invalidFields
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: redirectUrl
  type: string
- container: ''
  name: resultCode
  type: string
property_count: 12
provider_name: Adyen
provider_slug: adyen
slug: adyen-hosted-onboarding-get-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
