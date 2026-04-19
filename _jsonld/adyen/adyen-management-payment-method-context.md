---
class_count: 3
classes:
- PaymentMethodResponse
- PaymentMethod
- PaymentMethodSetupInfo
context_file: json-ld/adyen-management-payment-method-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adyen/refs/heads/main/json-ld/adyen-management-payment-method-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adyen Management Payment Method from Adyen.
layout: jsonld
name: Adyen Management Payment Method Context
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
  name: Links
  type: string
- container: set
  name: data
  type: string
- container: ''
  name: itemsTotal
  type: integer
- container: ''
  name: pagesTotal
  type: integer
- container: set
  name: typesWithErrors
  type: string
- container: ''
  name: afterpayTouch
  type: string
- container: ''
  name: allowed
  type: boolean
- container: ''
  name: applePay
  type: string
- container: ''
  name: bcmc
  type: string
- container: ''
  name: businessLineId
  type: string
- container: ''
  name: cartesBancaires
  type: string
- container: ''
  name: clearpay
  type: string
- container: set
  name: countries
  type: string
- container: ''
  name: cup
  type: string
- container: set
  name: currencies
  type: string
- container: set
  name: customRoutingFlags
  type: string
- container: ''
  name: diners
  type: string
- container: ''
  name: discover
  type: string
- container: ''
  name: eftposAustralia
  type: string
- container: ''
  name: enabled
  type: boolean
- container: ''
  name: giroPay
  type: string
- container: ''
  name: girocard
  type: string
- container: ''
  name: googlePay
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: ideal
  type: string
- container: ''
  name: interacCard
  type: string
- container: ''
  name: jcb
  type: string
- container: ''
  name: klarna
  type: string
- container: ''
  name: maestro
  type: string
- container: ''
  name: mc
  type: string
- container: ''
  name: mealVoucherFr
  type: string
- container: ''
  name: paypal
  type: string
- container: ''
  name: reference
  type: string
- container: ''
  name: shopperInteraction
  type: string
- container: ''
  name: sofort
  type: string
- container: set
  name: storeIds
  type: string
- container: ''
  name: swish
  type: string
- container: ''
  name: twint
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: verificationStatus
  type: string
- container: ''
  name: vipps
  type: string
- container: ''
  name: visa
  type: string
property_count: 42
provider_name: Adyen
provider_slug: adyen
slug: adyen-management-payment-method-context
tags:
- Payments
- Financial Services
- Fintech
- JSON-LD
- Linked Data
- Semantic Web
---
