---
description: Standard error response
layout: schema
name: ErrorResponse
properties_list:
- description: Unique identifier for this error occurrence
  name: errorId
  type: string
- description: Human-readable error description
  name: errorMessage
  type: string
- description: The HTTP status code as a string
  name: httpStatus
  type: string
- description: The request path that triggered the error
  name: path
  type: string
- description: When the error occurred
  name: timestamp
  type: string
- description: Detailed field-level validation failures
  name: validationErrors
  type: array
provider_name: SAP Concur
provider_slug: sap-concur
schema_file: json-schema/sap-concur-expense-error-response-schema.json
slug: sap-concur-expense-error-response
tags:
- Business Travel
- Expense Management
- Financial Services
- Invoice Management
- Travel Management
title: ErrorResponse
---
