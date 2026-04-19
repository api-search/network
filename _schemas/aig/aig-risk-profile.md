---
description: Risk profile for an insured entity
layout: schema
name: RiskProfile
properties_list:
- description: Name of the insured entity
  name: entity_name
  type: string
- description: Industry classification
  name: industry
  type: string
- description: NAICS industry code
  name: naics_code
  type: string
- description: Annual revenue in USD
  name: annual_revenue
  type: number
- description: Number of employees
  name: employee_count
  type: integer
- description: List of business locations
  name: locations
  type: array
- description: Historical loss records
  name: loss_history
  type: array
provider_name: AIG
provider_slug: aig
schema_file: json-schema/aig-risk-profile-schema.json
slug: aig-risk-profile
tags:
- Insurance
- Financial Services
- Property Casualty
- Cyber Insurance
- Enterprise
title: RiskProfile
---
