---
description: Response confirming partner miles credit
layout: schema
name: PartnerMilesResponse
properties_list:
- description: Unique transaction identifier
  name: transactionId
  type: string
- description: Member number
  name: memberId
  type: string
- description: Miles credited
  name: miles
  type: integer
- description: Updated mile balance
  name: newBalance
  type: integer
- description: Transaction status
  name: status
  type: string
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-mileage-plan-partner-miles-response-schema.json
slug: alaska-air-mileage-plan-partner-miles-response
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: PartnerMilesResponse
---
