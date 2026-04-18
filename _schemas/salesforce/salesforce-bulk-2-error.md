---
description: An error response from the Salesforce Bulk API 2.0.
layout: schema
name: Error
properties_list:
- description: Human-readable description of the error.
  name: message
  type: string
- description: Salesforce error code identifying the type of error.
  name: errorCode
  type: string
- description: List of field names related to the error, if applicable.
  name: fields
  type: array
provider_name: Salesforce
provider_slug: salesforce
schema_file: json-schema/salesforce-bulk-2-error-schema.json
slug: salesforce-bulk-2-error
tags:
- AI
- Analytics
- Cloud
- Commerce
- CRM
- Customer Service
- Enterprise
- Marketing
- Platform
- Sales
title: Error
---
