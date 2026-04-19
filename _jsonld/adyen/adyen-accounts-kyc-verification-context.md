---
class_count: 1
classes:
- KYCVerificationResult
context_file: json-ld/adyen-accounts-kyc-verification-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-accounts-kyc-verification-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Accounts Kyc Verification from Adyen.
layout: jsonld
name: Adyen Accounts Kyc Verification Context
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
  name: accountHolder
  type: string
- container: set
  name: legalArrangements
  type: string
- container: set
  name: legalArrangementsEntities
  type: string
- container: set
  name: payoutMethods
  type: string
- container: set
  name: shareholders
  type: string
- container: set
  name: signatories
  type: string
- container: set
  name: ultimateParentCompany
  type: string
property_count: 7
provider_name: Adyen
provider_slug: adyen
slug: adyen-accounts-kyc-verification-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
