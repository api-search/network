---
description: A company creditworthiness grade from Allianz Trade
layout: schema
name: CompanyGrade
properties_list:
- description: Unique identifier for the company grade
  name: gradeId
  type: string
- description: Trade credit insurance policy identifier
  name: policyId
  type: string
- description: Name of the graded company
  name: companyName
  type: string
- description: Official company registration number
  name: companyRegistrationNumber
  type: string
- description: ISO 3166-1 alpha-2 country code
  name: country
  type: string
- description: Creditworthiness grade letter
  name: grade
  type: string
- description: Numeric score underlying the grade (0-100)
  name: gradeScore
  type: integer
- description: ISO 4217 currency code
  name: currency
  type: string
- description: Approved credit limit amount
  name: creditLimit
  type: number
- description: Originally requested credit limit
  name: requestedCreditLimit
  type: number
- description: Date until which the grade is valid
  name: validUntil
  type: string
- description: Timestamp when the grade was issued
  name: gradedAt
  type: string
provider_name: Allianz Trade
provider_slug: allianz-trade-online
schema_file: json-schema/trade-company-grade-company_grade-schema.json
slug: trade-company-grade-company_grade
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
title: CompanyGrade
---
