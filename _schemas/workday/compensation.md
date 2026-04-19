---
description: Represents compensation data for a worker in Workday, including salary plans, allowance plans, bonus plans, and total compensation details.
layout: schema
name: Compensation
properties_list:
- description: The Workday ID of the compensation record.
  name: id
  type: string
- description: A display descriptor for the compensation record.
  name: descriptor
  type: string
- description: The worker this compensation belongs to.
  name: worker
  type: object
- description: The effective date of the compensation.
  name: effectiveDate
  type: string
- description: The compensation plans assigned to the worker.
  name: compensationPlans
  type: array
- description: The total base pay amount across all salary plans.
  name: totalBasePayAmount
  type: number
- description: The annualized total base pay amount.
  name: totalBasePayAnnualizedAmount
  type: number
- description: Total salary and allowances combined.
  name: totalSalaryAndAllowancesAmount
  type: number
- description: The primary compensation basis amount.
  name: primaryCompensationBasis
  type: number
- description: The currency for compensation amounts.
  name: currency
  type: object
- description: The pay frequency (e.g., Annual, Monthly, Bi-Weekly, Weekly).
  name: frequency
  type: object
- description: The compensation grade.
  name: compensationGrade
  type: object
- description: The compensation grade profile.
  name: compensationGradeProfile
  type: object
- description: The compensation step within the grade.
  name: compensationStep
  type: object
- description: The compa-ratio (current pay relative to midpoint of compensation range).
  name: compaRatio
  type: number
- description: The range position (where in the pay range the worker falls).
  name: rangePosition
  type: number
- description: The pay rate type (e.g., Salary, Hourly).
  name: payRateType
  type: object
- description: A link to the full compensation resource.
  name: href
  type: string
provider_name: Workday
provider_slug: workday
schema_file: json-schema/compensation.json
slug: compensation
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
title: Compensation
---
