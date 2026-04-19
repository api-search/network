---
class_count: 5
classes:
- AccountHolderCapability
- AccountHolderInfo
- AccountHolder
- AccountHolderUpdateRequest
- description
context_file: json-ld/adyen-configuration-account-holder-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-configuration-account-holder-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Configuration Account Holder from Adyen.
layout: jsonld
name: Adyen Configuration Account Holder Context
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
  name: allowed
  type: boolean
- container: ''
  name: allowedLevel
  type: string
- container: ''
  name: allowedSettings
  type: string
- container: ''
  name: enabled
  type: boolean
- container: set
  name: problems
  type: string
- container: ''
  name: requested
  type: boolean
- container: ''
  name: requestedLevel
  type: string
- container: ''
  name: requestedSettings
  type: string
- container: set
  name: transferInstruments
  type: string
- container: ''
  name: verificationStatus
  type: string
- container: ''
  name: balancePlatform
  type: string
- container: ''
  name: capabilities
  type: reference
- container: ''
  name: contactDetails
  type: string
- container: ''
  name: legalEntityId
  type: string
- container: ''
  name: metadata
  type: reference
- container: ''
  name: migratedAccountHolderCode
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: timeZone
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: primaryBalanceAccount
  type: string
- container: ''
  name: status
  type: string
- container: set
  name: verificationDeadlines
  type: string
property_count: 22
provider_name: Adyen
provider_slug: adyen
slug: adyen-configuration-account-holder-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
