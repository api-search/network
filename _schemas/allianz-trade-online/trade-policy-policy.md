---
description: A trade credit insurance policy from Allianz Trade
layout: schema
name: Policy
properties_list:
- description: Unique identifier for the policy
  name: policyId
  type: string
- description: Official Allianz Trade policy number
  name: policyNumber
  type: string
- description: Legal name of the policy holder
  name: policyHolderName
  type: string
- description: Type of trade credit insurance policy
  name: policyType
  type: string
- description: Current status of the policy
  name: policyStatus
  type: string
- description: ISO 4217 policy currency code
  name: currency
  type: string
- description: Maximum total coverage amount under the policy
  name: maxCoverageAmount
  type: number
- description: Percentage of loss covered by the policy
  name: coveragePercentage
  type: integer
- description: Policy start date
  name: startDate
  type: string
- description: Policy end date
  name: endDate
  type: string
- description: ISO 3166-1 alpha-2 country code for the policy
  name: country
  type: string
- description: Timestamp when the policy was created
  name: createdAt
  type: string
provider_name: Allianz Trade
provider_slug: allianz-trade-online
schema_file: json-schema/trade-policy-policy-schema.json
slug: trade-policy-policy
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
title: Policy
---
