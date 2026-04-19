---
description: Request to report partner miles for a Mileage Plan member
layout: schema
name: PartnerMilesRequest
properties_list:
- description: Mileage Plan member number
  name: memberId
  type: string
- description: Registered partner identifier
  name: partnerId
  type: string
- description: Type of partner activity
  name: activityType
  type: string
- description: Date of partner activity
  name: activityDate
  type: string
- description: Transaction amount in partner currency
  name: activityAmount
  type: number
- description: Currency code
  name: currency
  type: string
- description: Miles to credit
  name: miles
  type: integer
- description: Partner activity reference number
  name: referenceId
  type: string
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-mileage-plan-partner-miles-request-schema.json
slug: alaska-air-mileage-plan-partner-miles-request
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: PartnerMilesRequest
---
