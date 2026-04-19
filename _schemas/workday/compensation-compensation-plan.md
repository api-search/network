---
description: ''
layout: schema
name: CompensationPlan
properties_list:
- description: The Workday ID of the compensation plan.
  name: id
  type: string
- description: A display descriptor for the plan.
  name: descriptor
  type: string
- description: The type of compensation plan (e.g., Salary, Allowance, Bonus).
  name: compensationPlanType
  type: string
- description: The compensation amount.
  name: amount
  type: number
- description: ''
  name: effectiveDate
  type: string
provider_name: Workday
provider_slug: workday
schema_file: json-schema/compensation-compensation-plan-schema.json
slug: compensation-compensation-plan
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
title: CompensationPlan
---
