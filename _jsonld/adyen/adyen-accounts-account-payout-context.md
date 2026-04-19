---
class_count: 1
classes:
- AccountPayoutState
context_file: json-ld/adyen-accounts-account-payout-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-accounts-account-payout-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Accounts Account Payout from Adyen.
layout: jsonld
name: Adyen Accounts Account Payout Context
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
  name: allowPayout
  type: boolean
- container: ''
  name: disableReason
  type: string
- container: ''
  name: disabled
  type: boolean
- container: ''
  name: notAllowedReason
  type: string
- container: ''
  name: payoutLimit
  type: string
- container: ''
  name: tierNumber
  type: integer
property_count: 6
provider_name: Adyen
provider_slug: adyen
slug: adyen-accounts-account-payout-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
