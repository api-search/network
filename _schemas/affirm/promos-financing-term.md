---
description: A single available financing term option including APR and payment details.
layout: schema
name: FinancingTerm
properties_list:
- description: Purchase amount this term applies to, in cents.
  name: amount
  type: integer
- description: Type of financing loan (e.g., split_pay, installment).
  name: loan_type
  type: string
- description: Annual percentage rate for this financing term.
  name: apr
  type: number
- description: Monthly installment payment amount in cents.
  name: installment_amount
  type: integer
- description: Total number of installment payments.
  name: installment_count
  type: integer
- description: Total interest charged over the life of the loan in cents.
  name: interest_amount
  type: integer
- description: Total amount paid including principal and interest, in cents.
  name: total_amount
  type: integer
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/promos-financing-term-schema.json
slug: promos-financing-term
tags: []
title: FinancingTerm
---
