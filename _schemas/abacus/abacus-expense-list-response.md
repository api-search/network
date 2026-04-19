---
description: Paginated list of expenses
layout: schema
name: ExpenseListResponse
properties_list:
- description: ''
  name: expenses
  type: array
- description: Total number of expenses
  name: total
  type: integer
- description: Current page number
  name: page
  type: integer
- description: Number of results per page
  name: per_page
  type: integer
provider_name: Abacus
provider_slug: abacus
schema_file: json-schema/abacus-expense-list-response-schema.json
slug: abacus-expense-list-response
tags:
- Accounting
- Expense Management
- Finance
- Reimbursement
title: ExpenseListResponse
---
