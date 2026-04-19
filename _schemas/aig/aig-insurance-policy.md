---
description: An AIG insurance policy covering insured risks
layout: schema
name: InsurancePolicy
properties_list:
- description: Unique policy identifier
  name: policy_number
  type: string
- description: Type of insurance policy
  name: policy_type
  type: string
- description: Name of the insured entity
  name: insured_name
  type: string
- description: Policy effective date
  name: effective_date
  type: string
- description: Policy expiration date
  name: expiration_date
  type: string
- description: Annual premium amount in USD
  name: premium
  type: number
- description: Policy coverage limit in USD
  name: coverage_limit
  type: number
- description: Policy deductible amount in USD
  name: deductible
  type: number
- description: Policy status
  name: status
  type: string
provider_name: AIG
provider_slug: aig
schema_file: json-schema/aig-insurance-policy-schema.json
slug: aig-insurance-policy
tags:
- Insurance
- Financial Services
- Property Casualty
- Cyber Insurance
- Enterprise
title: InsurancePolicy
---
