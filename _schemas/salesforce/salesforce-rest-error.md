---
description: An error response from the Salesforce REST API, describing the problem with the request.
layout: schema
name: Error
properties_list:
- description: Human-readable description of the error.
  name: message
  type: string
- description: Salesforce error code (e.g., MALFORMED_QUERY, INVALID_FIELD, REQUIRED_FIELD_MISSING).
  name: errorCode
  type: string
- description: List of field names related to the error, if applicable (e.g., for field validation errors).
  name: fields
  type: array
provider_name: Salesforce
provider_slug: salesforce
schema_file: json-schema/salesforce-rest-error-schema.json
slug: salesforce-rest-error
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
