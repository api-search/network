---
class_count: 5
classes:
- CreateAccountHolderRequest
- CreateAccountHolderResponse
- CreateAccountRequest
- CreateAccountResponse
- description
context_file: json-ld/adyen-accounts-create-account-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-accounts-create-account-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Accounts Create Account from Adyen.
layout: jsonld
name: Adyen Accounts Create Account Context
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
  name: accountHolderDetails
  type: string
- container: ''
  name: createDefaultAccount
  type: boolean
- container: ''
  name: legalEntity
  type: string
- container: ''
  name: primaryCurrency
  type: string
- container: ''
  name: processingTier
  type: integer
- container: ''
  name: verificationProfile
  type: string
- container: ''
  name: accountCode
  type: string
- container: ''
  name: accountHolderStatus
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
- container: ''
  name: verification
  type: string
- container: ''
  name: bankAccountUUID
  type: string
- container: ''
  name: metadata
  type: reference
- container: ''
  name: payoutMethodCode
  type: string
- container: ''
  name: payoutSchedule
  type: string
- container: ''
  name: payoutScheduleReason
  type: string
- container: ''
  name: payoutSpeed
  type: string
- container: ''
  name: status
  type: string
property_count: 20
provider_name: Adyen
provider_slug: adyen
slug: adyen-accounts-create-account-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
