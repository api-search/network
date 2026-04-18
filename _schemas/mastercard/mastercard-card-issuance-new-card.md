---
description: ''
layout: schema
name: NewCard
properties_list:
- description: Indicates whether number should be printed on the physical card or not. <BR/> Not applicable while issuing existing non-personalized card.
  name: numberless
  type: boolean
- description: Indicates whether instant card is required be generated or not. <BR/> It will be always considered as true in case of SVC/LVC card issuance irrespective of input value. <BR/>Not applicable while issui
  name: instant
  type: boolean
- description: Date on which card is delivered or handed over to client. <br/> Format - It is expressed in ISO 8601 - `YYYY-MM-DD`
  name: deliveryDate
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-new-card-schema.json
slug: mastercard-card-issuance-new-card
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: NewCard
---
