---
description: A custom field value configured by the organization. Field IDs follow patterns like custom1-custom40 and orgUnit1-orgUnit6.
layout: schema
name: CustomData
properties_list:
- description: The identifier of the custom field (e.g., custom1, orgUnit1)
  name: id
  type: string
- description: The value assigned to the custom field
  name: value
  type: string
- description: Whether the current value passes validation rules
  name: isValid
  type: boolean
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-custom-data-schema.json
slug: sap-concur-expense-custom-data
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: CustomData
---
