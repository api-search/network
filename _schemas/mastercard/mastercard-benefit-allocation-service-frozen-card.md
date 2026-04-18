---
description: ''
layout: schema
name: FrozenCard
properties_list:
- description: 16 or 19 digit PAN number that will be frozen/unfrozen.
  name: cardNumber
  type: integer
- description: Date at which the freeze will be effective. Date should be in YYYY-MM-DD format.
  name: date
  type: string
- description: Variable to change whether or not the card number is frozen. True for freeze and false for unfreeze.
  name: isFrozen
  type: boolean
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-benefit-allocation-service-frozen-card-schema.json
slug: mastercard-benefit-allocation-service-frozen-card
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: FrozenCard
---
