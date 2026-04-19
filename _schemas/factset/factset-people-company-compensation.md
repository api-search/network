---
description: List of executives and their compensation details for the specified company identifier.
layout: schema
name: companyCompensation
properties_list:
- description: FactSet Name of the person
  name: name
  type: string
- description: Factset Entity Identifier for the Person
  name: personId
  type: string
- description: The requested Position Title
  name: title
  type: string
- description: Salary of the person. Expressed in USD and raw units.
  name: salary
  type: number
- description: Bonus of the executive during the fiscal year. Expressed in USD and raw units.
  name: bonus
  type: number
- description: Stock awards for the person. Expressed in USD and raw units.
  name: stockAwards
  type: number
- description: Option Awards for the person. Expressed in USD and raw units.
  name: optionsAwards
  type: number
- description: All the other compensations which are not explicitly defined as salary, bonus, stock awards, or options awards. Expressed in USD and raw units.
  name: otherCompensation
  type: number
- description: The sum of all compensation for the requested person as reported by the company. Expressed in USD and raw units.
  name: totalCompensation
  type: number
- description: All the earnings pursuant to awards under non-equity incentive plans. Expressed in USD and raw units.
  name: nonEquityIncentivePlanComp
  type: number
- description: All the other nonqualified defined contribution which are not tax qualified and other contributions. Expressed in USD and raw units.
  name: nonQualifiedCompEarnings
  type: number
- description: The most recent year of compensation is expressed as 'YYYY' as opposed to 'YYYY-MM-DD' format.
  name: compensationYear
  type: string
- description: Original identifier used for the request.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-people-company-compensation-schema.json
slug: factset-people-company-compensation
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: companyCompensation
---
