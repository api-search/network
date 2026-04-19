---
description: Error response returned when a request fails.
layout: schema
name: ErrorResponse
properties_list:
- description: The error type identifier.
  name: '@type'
  type: string
- description: The HTTP status code.
  name: statusCode
  type: integer
- description: A human-readable error message.
  name: message
  type: string
- description: A detailed description of the error.
  name: description
  type: string
- description: The unique request ID for troubleshooting.
  name: requestId
  type: string
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-error-response-schema.json
slug: informatica-platform-rest-error-response
tags:
- Address Verification
- B2B Gateway
- Cloud Services
- Data Governance
- Data Integration
- Data Profiling
- Data Quality
- Enterprise Software
- ETL
- IDMC
- IICS
- Master Data Management
- Reference Data Management
title: ErrorResponse
---
