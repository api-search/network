---
description: Configuration parameters for creating a new Bulk API 2.0 query job.
layout: schema
name: QueryJobRequest
properties_list:
- description: The query operation to perform. Use query to retrieve active records only, or queryAll to include soft-deleted and archived records.
  name: operation
  type: string
- description: The SOQL query to execute. The query result will be available as CSV data after the job completes.
  name: query
  type: string
- description: The format of the results. Currently only CSV is supported.
  name: contentType
  type: string
- description: The delimiter character used between fields in the CSV output.
  name: columnDelimiter
  type: string
- description: The line ending character used in the CSV output.
  name: lineEnding
  type: string
provider_name: Salesforce
provider_slug: salesforce
schema_file: json-schema/salesforce-bulk-2-query-job-request-schema.json
slug: salesforce-bulk-2-query-job-request
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
title: QueryJobRequest
---
