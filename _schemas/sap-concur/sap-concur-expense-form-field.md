---
description: A configured form field with its metadata, display properties, and validation rules.
layout: schema
name: FormField
properties_list:
- description: The field identifier
  name: id
  type: string
- description: The localized display label
  name: label
  type: string
- description: The UI control type for rendering
  name: controlType
  type: string
- description: The data type of the field value
  name: dataType
  type: string
- description: Whether the field is mandatory
  name: isRequired
  type: boolean
- description: Whether this is a customer-configured custom field
  name: isCustom
  type: boolean
- description: Maximum allowed character length
  name: maxLength
  type: integer
- description: Display order sequence number
  name: sequence
  type: integer
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-form-field-schema.json
slug: sap-concur-expense-form-field
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: FormField
---
