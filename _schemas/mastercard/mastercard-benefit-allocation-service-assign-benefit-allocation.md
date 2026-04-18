---
description: ''
layout: schema
name: AssignBenefitAllocation
properties_list:
- description: 16 or 19 digit PAN number that will have a segment assigned to it.
  name: cardNumber
  type: integer
- description: List of segments that will be assigned to the pan number. Only accepts arrays containing one segment.
  name: segments
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-benefit-allocation-service-assign-benefit-allocation-schema.json
slug: mastercard-benefit-allocation-service-assign-benefit-allocation
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: AssignBenefitAllocation
---
