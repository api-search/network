---
description: ''
layout: schema
name: ReplaceBenefitAllocation
properties_list:
- description: 16 or 19 digit PAN number that will have its segment replaced.
  name: cardNumber
  type: integer
- description: Unique identifier representing a group of benefit bundles that will be expired and replaced.
  name: oldSegmentCode
  type: string
- description: Unique identifier representing the new group of benefit bundles that will be assigned.
  name: newSegmentCode
  type: string
- description: Date at which the new segment will go in effect. Date should be in YYYY-MM-DD format.
  name: effectiveDate
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-benefit-allocation-service-replace-benefit-allocation-schema.json
slug: mastercard-benefit-allocation-service-replace-benefit-allocation
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: ReplaceBenefitAllocation
---
