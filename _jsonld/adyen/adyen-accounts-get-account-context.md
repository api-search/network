---
class_count: 4
classes:
- GetAccountHolderRequest
- GetAccountHolderResponse
- GetAccountHolderStatusResponse
- description
context_file: json-ld/adyen-accounts-get-account-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-accounts-get-account-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Accounts Get Account from Adyen.
layout: jsonld
name: Adyen Accounts Get Account Context
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
  name: showDetails
  type: boolean
- container: ''
  name: accountHolderDetails
  type: string
- container: ''
  name: accountHolderStatus
  type: string
- container: set
  name: accounts
  type: string
- container: set
  name: invalidFields
  type: string
- container: ''
  name: legalEntity
  type: string
- container: ''
  name: migrationData
  type: string
- container: ''
  name: primaryCurrency
  type: string
- container: ''
  name: pspReference
  type: string
- container: ''
  name: resultCode
  type: string
- container: ''
  name: systemUpToDateTime
  type: dateTime
- container: ''
  name: verification
  type: string
- container: ''
  name: verificationProfile
  type: string
property_count: 15
provider_name: Adyen
provider_slug: adyen
slug: adyen-accounts-get-account-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
