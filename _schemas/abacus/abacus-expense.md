---
description: An expense report submitted by a member
layout: schema
name: Expense
properties_list:
- description: Unique expense identifier
  name: id
  type: string
- description: ID of the member who submitted the expense
  name: member_id
  type: string
- description: Expense amount
  name: amount
  type: number
- description: Currency code (ISO 4217)
  name: currency
  type: string
- description: Expense category
  name: category
  type: string
- description: Description of the expense
  name: description
  type: string
- description: Date of the expense
  name: date
  type: string
- description: Current status of the expense
  name: status
  type: string
- description: URL to the uploaded receipt
  name: receipt_url
  type: string
- description: Timestamp when the expense was created
  name: created_at
  type: string
- description: Timestamp when the expense was last updated
  name: updated_at
  type: string
provider_name: Abacus
provider_slug: abacus
schema_file: json-schema/abacus-expense-schema.json
slug: abacus-expense
tags:
- Accounting
- Expense Management
- Finance
- Reimbursement
title: Expense
---
