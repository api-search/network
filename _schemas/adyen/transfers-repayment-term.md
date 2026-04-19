---
description: RepaymentTerm schema from Adyen API
layout: schema
name: RepaymentTerm
properties_list:
- description: The estimated term for repaying the grant, in days.
  name: estimatedDays
  type: integer
- description: The maximum term for repaying the grant, in days. Only applies when `contractType` is **loan**.
  name: maximumDays
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-repayment-term-schema.json
slug: transfers-repayment-term
tags:
- Payments
- Financial Services
- Fintech
title: RepaymentTerm
---
