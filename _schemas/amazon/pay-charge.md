---
description: Charge schema from Amazon Pay API
layout: schema
name: Charge
properties_list:
- description: ''
  name: chargeId
  type: string
- description: ''
  name: chargePermissionId
  type: string
- description: ''
  name: chargeAmount
  type: object
- description: ''
  name: captureAmount
  type: object
- description: ''
  name: refundedAmount
  type: object
- description: ''
  name: softDescriptor
  type: string
- description: ''
  name: statusDetails
  type: object
- description: ''
  name: creationTimestamp
  type: string
- description: ''
  name: expirationTimestamp
  type: string
provider_name: Amazon
provider_slug: amazon
schema_file: json-schema/pay-charge-schema.json
slug: pay-charge
tags:
- Amazon
- Advertising
- Alexa
- E-Commerce
- Marketplace
- Payments
- Voice
title: Charge
---
