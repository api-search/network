---
description: An expense category classification
layout: schema
name: ExpenseType
properties_list:
- description: The expense type identifier (e.g., BRKFT, LODNG, AIRFR)
  name: id
  type: string
- description: The localized display name
  name: name
  type: string
- description: The expense type code
  name: code
  type: string
- description: Whether this type has been deactivated
  name: isDeleted
  type: boolean
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-expense-type-schema.json
slug: sap-concur-expense-expense-type
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: ExpenseType
---
