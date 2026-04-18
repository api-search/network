---
description: Travel allowance (per diem) data associated with an expense
layout: schema
name: TravelAllowance
properties_list:
- description: Whether this expense is part of a travel allowance
  name: isExpensePartOfTravelAllowance
  type: boolean
- description: Identifier of the daily travel allowance
  name: dailyTravelAllowanceId
  type: string
- description: The daily allowance limit amount
  name: dailyLimitAmount
  type: number
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-travel-allowance-schema.json
slug: sap-concur-expense-travel-allowance
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: TravelAllowance
---
