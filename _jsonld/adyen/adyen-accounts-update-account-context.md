---
class_count: 6
classes:
- UpdateAccountHolderRequest
- UpdateAccountHolderResponse
- UpdateAccountHolderStateRequest
- UpdateAccountRequest
- UpdateAccountResponse
- description
context_file: json-ld/adyen-accounts-update-account-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-accounts-update-account-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Accounts Update Account from Adyen.
layout: jsonld
name: Adyen Accounts Update Account Context
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
  name: disable
  type: boolean
- container: ''
  name: reason
  type: string
- container: ''
  name: stateType
  type: string
- container: ''
  name: accountCode
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
  name: payoutSpeed
  type: string
property_count: 20
provider_name: Adyen
provider_slug: adyen
slug: adyen-accounts-update-account-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
