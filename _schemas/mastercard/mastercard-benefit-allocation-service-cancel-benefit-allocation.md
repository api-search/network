---
description: ''
layout: schema
name: CancelBenefitAllocation
properties_list:
- description: 16 or 19 digit PAN number that will have it's segment expired/cancelled.
  name: cardNumber
  type: integer
- description: List of segments assigned to the card number that will be cancelled. Only accepts arrays containing one segment.
  name: segments
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-benefit-allocation-service-cancel-benefit-allocation-schema.json
slug: mastercard-benefit-allocation-service-cancel-benefit-allocation
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: CancelBenefitAllocation
---
