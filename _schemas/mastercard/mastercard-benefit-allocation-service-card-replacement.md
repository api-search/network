---
description: ''
layout: schema
name: CardReplacement
properties_list:
- description: 16 or 19 digit PAN number that will be expired and replaced along with its benefit bundles.
  name: oldCardNumber
  type: integer
- description: New 16 or 19 digit PAN number that will have the same unexpired set of benefits as the old card number.
  name: newCardNumber
  type: integer
- description: Date at which the replace will be effective. Date should be in YYYY-MM-DD format.
  name: effectiveDate
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-benefit-allocation-service-card-replacement-schema.json
slug: mastercard-benefit-allocation-service-card-replacement
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: CardReplacement
---
