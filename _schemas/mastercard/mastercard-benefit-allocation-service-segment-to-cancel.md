---
description: ''
layout: schema
name: SegmentToCancel
properties_list:
- description: Identifier that represents a group of benefit bundles to be cancelled.
  name: code
  type: string
- description: Date at which the benefit bundles associated to the segment code will be cancelled. Date should be in YYYY-MM-DD format.
  name: expiryDate
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-benefit-allocation-service-segment-to-cancel-schema.json
slug: mastercard-benefit-allocation-service-segment-to-cancel
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: SegmentToCancel
---
