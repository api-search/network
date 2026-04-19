---
class_count: 1
classes:
- AccountInfo
context_file: json-ld/adyen-checkout-account-info-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-checkout-account-info-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Checkout Account Info from Adyen.
layout: jsonld
name: Adyen Checkout Account Info Context
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
  name: accountAgeIndicator
  type: string
- container: ''
  name: accountChangeDate
  type: dateTime
- container: ''
  name: accountChangeIndicator
  type: string
- container: ''
  name: accountCreationDate
  type: dateTime
- container: ''
  name: accountType
  type: string
- container: ''
  name: addCardAttemptsDay
  type: integer
- container: ''
  name: deliveryAddressUsageDate
  type: dateTime
- container: ''
  name: deliveryAddressUsageIndicator
  type: string
- container: ''
  name: homePhone
  type: string
- container: ''
  name: mobilePhone
  type: string
- container: ''
  name: passwordChangeDate
  type: dateTime
- container: ''
  name: passwordChangeIndicator
  type: string
- container: ''
  name: pastTransactionsDay
  type: integer
- container: ''
  name: pastTransactionsYear
  type: integer
- container: ''
  name: paymentAccountAge
  type: dateTime
- container: ''
  name: paymentAccountIndicator
  type: string
- container: ''
  name: purchasesLast6Months
  type: integer
- container: ''
  name: suspiciousActivity
  type: boolean
- container: ''
  name: workPhone
  type: string
property_count: 19
provider_name: Adyen
provider_slug: adyen
slug: adyen-checkout-account-info-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
