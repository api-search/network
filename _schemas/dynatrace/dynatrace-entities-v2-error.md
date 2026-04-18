---
description: Details of an API error.
layout: schema
name: Error
properties_list:
- description: The HTTP status code of the error.
  name: code
  type: integer
- description: A human-readable description of the error.
  name: message
  type: string
- description: A list of constraint violations for validation errors (HTTP 400).
  name: constraintViolations
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-entities-v2-error-schema.json
slug: dynatrace-entities-v2-error
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
title: Error
---
