---
class_count: 3
classes:
- PayoutAccountHolderRequest
- PayoutAccountHolderResponse
- description
context_file: json-ld/adyen-funds-payout-account-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-funds-payout-account-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Funds Payout Account from Adyen.
layout: jsonld
name: Adyen Funds Payout Account Context
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
  name: accountCode
  type: string
- container: ''
  name: accountHolderCode
  type: string
- container: ''
  name: amount
  type: string
- container: ''
  name: bankAccountUUID
  type: string
- container: ''
  name: merchantReference
  type: string
- container: ''
  name: payoutMethodCode
  type: string
- container: ''
  name: payoutSpeed
  type: string
- container: set
  name: invalidFields
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: resultCode
  type: string
property_count: 10
provider_name: Adyen
provider_slug: adyen
slug: adyen-funds-payout-account-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
