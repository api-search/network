---
description: Configuration parameters for creating a new Bulk API 2.0 ingest job.
layout: schema
name: IngestJobRequest
properties_list:
- description: 'The DML operation to perform on the records. Use insert to create new records, update to modify existing records, upsert to create or update based on an external ID, delete to soft-delete records, or '
  name: operation
  type: string
- description: The API name of the Salesforce SObject type for this job (e.g., Account, Contact, MyCustomObject__c).
  name: object
  type: string
- description: Required for upsert operations. The API name of the external ID field used to match records for upsert.
  name: externalIdFieldName
  type: string
- description: The format of the data to be uploaded. Currently only CSV is supported.
  name: contentType
  type: string
- description: The line ending character used in the uploaded CSV data. Use LF for Unix-style line endings or CRLF for Windows-style.
  name: lineEnding
  type: string
- description: The delimiter character used between fields in the CSV data. Defaults to COMMA.
  name: columnDelimiter
  type: string
- description: The ID of an assignment rule to apply when inserting or updating Case or Lead records.
  name: assignmentRuleId
  type: string
provider_name: Salesforce
provider_slug: salesforce
schema_file: json-schema/salesforce-bulk-2-ingest-job-request-schema.json
slug: salesforce-bulk-2-ingest-job-request
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
title: IngestJobRequest
---
