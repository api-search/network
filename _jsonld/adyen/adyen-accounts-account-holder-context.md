---
class_count: 3
classes:
- AccountHolderDetails
- AccountHolderStatus
- email
context_file: json-ld/adyen-accounts-account-holder-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-accounts-account-holder-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Accounts Account Holder from Adyen.
layout: jsonld
name: Adyen Accounts Account Holder Context
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
  name: address
  type: string
- container: set
  name: bankAccountDetails
  type: string
- container: ''
  name: bankAggregatorDataReference
  type: string
- container: ''
  name: businessDetails
  type: string
- container: ''
  name: fullPhoneNumber
  type: string
- container: ''
  name: individualDetails
  type: string
- container: ''
  name: lastReviewDate
  type: string
- container: set
  name: legalArrangements
  type: string
- container: ''
  name: merchantCategoryCode
  type: string
- container: ''
  name: metadata
  type: reference
- container: set
  name: payoutMethods
  type: string
- container: ''
  name: principalBusinessAddress
  type: string
- container: set
  name: storeDetails
  type: string
- container: ''
  name: webAddress
  type: string
- container: set
  name: events
  type: string
- container: ''
  name: payoutState
  type: string
- container: ''
  name: processingState
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: statusReason
  type: string
property_count: 19
provider_name: Adyen
provider_slug: adyen
slug: adyen-accounts-account-holder-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
