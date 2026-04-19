---
class_count: 3
classes:
- AceHardwareAffiliateReferral
- AceHardwareEdiPurchaseOrder
- description
context_file: json-ld/ace-hardware-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/ace-hardware/refs/heads/main/json-ld/ace-hardware-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Ace Hardware from Ace Hardware.
layout: jsonld
name: Ace Hardware Context
namespaces:
- prefix: ace
  uri: https://www.acehardware.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: aceItemNumber
  type: string
- container: ''
  name: affiliateId
  type: string
- container: ''
  name: affiliateName
  type: string
- container: ''
  name: clickDate
  type: dateTime
- container: ''
  name: commissionAmount
  type: decimal
- container: ''
  name: commissionRate
  type: decimal
- container: ''
  name: conversionDate
  type: dateTime
- container: ''
  name: currency
  type: string
- container: ''
  name: destinationUrl
  type: reference
- container: ''
  name: extendedCost
  type: decimal
- container: set
  name: lineItems
  type: string
- container: ''
  name: lineNumber
  type: integer
- container: ''
  name: orderDate
  type: date
- container: ''
  name: orderId
  type: string
- container: ''
  name: orderValue
  type: decimal
- container: ''
  name: poNumber
  type: string
- container: ''
  name: quantity
  type: integer
- container: ''
  name: referralId
  type: string
- container: ''
  name: referralUrl
  type: reference
- container: ''
  name: shipByDate
  type: date
- container: ''
  name: shipToAddress
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: totalAmount
  type: decimal
- container: ''
  name: unitCost
  type: decimal
- container: ''
  name: upc
  type: string
- container: ''
  name: vendorId
  type: string
- container: ''
  name: vendorName
  type: string
- container: ''
  name: vendorSku
  type: string
property_count: 28
provider_name: Ace Hardware
provider_slug: ace-hardware
slug: ace-hardware-context
tags:
- Retail
- Hardware
- Home Improvement
- Tools
- Paint
- Cooperative
- EDI
- Affiliate
- JSON-LD
- Linked Data
- Semantic Web
---
