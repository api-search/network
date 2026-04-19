---
description: Request body for requesting a company creditworthiness grade
layout: schema
name: CompanyGradeRequest
properties_list:
- description: Trade credit insurance policy identifier
  name: policyId
  type: string
- description: Name of the company to grade
  name: companyName
  type: string
- description: Official company registration number
  name: companyRegistrationNumber
  type: string
- description: ISO 3166-1 alpha-2 country code of the company
  name: country
  type: string
- description: Requested credit limit amount
  name: requestedCreditLimit
  type: number
- description: ISO 4217 currency code
  name: currency
  type: string
provider_name: Allianz Trade
provider_slug: allianz-trade-online
schema_file: json-schema/trade-company-grade-company_grade_request-schema.json
slug: trade-company-grade-company_grade_request
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
title: CompanyGradeRequest
---
