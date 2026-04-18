---
description: A payment method used for an expense
layout: schema
name: PaymentType
properties_list:
- description: The payment type identifier (e.g., CASH, CPAID)
  name: id
  type: string
- description: The localized display name
  name: name
  type: string
- description: The payment type code
  name: code
  type: string
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-payment-type-schema.json
slug: sap-concur-expense-payment-type
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: PaymentType
---
