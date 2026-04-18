---
description: An expense allocation that distributes an expense amount across cost centers, departments, or general ledger accounts.
layout: schema
name: Allocation
properties_list:
- description: Unique identifier of the allocation
  name: allocationId
  type: string
- description: The expense this allocation belongs to
  name: expenseId
  type: string
- description: The ledger account code
  name: accountCode
  type: string
- description: Account code for amounts exceeding policy limits
  name: overLimitAccountCode
  type: string
- description: The percentage of the total expense allocated (0-100)
  name: percentage
  type: number
- description: Whether this allocation was automatically created by the system (true) or manually created by a user (false)
  name: isSystemAllocation
  type: boolean
- description: Whether the allocation percentage has been modified
  name: isPercentEdited
  type: boolean
- description: Custom field values on the allocation
  name: customData
  type: array
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-allocation-schema.json
slug: sap-concur-expense-allocation
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: Allocation
---
