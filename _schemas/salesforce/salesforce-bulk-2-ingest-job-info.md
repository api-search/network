---
description: Detailed information about a Bulk API 2.0 ingest job, including its current state and processing statistics.
layout: schema
name: IngestJobInfo
properties_list:
- description: The unique identifier of the ingest job.
  name: id
  type: string
- description: The DML operation being performed by this job.
  name: operation
  type: string
- description: The API name of the SObject type being processed.
  name: object
  type: string
- description: The current state of a Bulk API 2.0 job, indicating where it is in its lifecycle.
  name: state
  type: string
- description: The date and time the job was created, in ISO 8601 format.
  name: createdDate
  type: string
- description: The date and time the job was last modified, in ISO 8601 format.
  name: systemModstamp
  type: string
- description: The number of records processed so far. Updated after processing completes.
  name: numberRecordsProcessed
  type: integer
- description: The number of records that failed during processing.
  name: numberRecordsFailed
  type: integer
- description: Total processing time in milliseconds.
  name: totalProcessingTime
  type: integer
- description: Error message if the job reached the Failed state. Describes the reason for failure.
  name: errorMessage
  type: string
- description: The content type of the data uploaded to this job.
  name: contentType
  type: string
- description: The line ending used in the uploaded data.
  name: lineEnding
  type: string
- description: The column delimiter used in the uploaded data.
  name: columnDelimiter
  type: string
- description: The external ID field name used for upsert operations. Only present for upsert jobs.
  name: externalIdFieldName
  type: string
- description: The job type (V2Ingest for Bulk API 2.0 ingest jobs).
  name: jobType
  type: string
- description: The Salesforce user ID of the user who created the job.
  name: createdById
  type: string
- description: The API version used to create the job.
  name: apiVersion
  type: number
provider_name: Salesforce
provider_slug: salesforce
schema_file: json-schema/salesforce-bulk-2-ingest-job-info-schema.json
slug: salesforce-bulk-2-ingest-job-info
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
title: IngestJobInfo
---
