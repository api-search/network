---
description: A Salesforce Bulk API 2.0 job definition representing either an ingest job (for inserting, updating, upserting, deleting, or hard-deleting records in bulk) or a query job (for extracting large volumes of records using SOQL). Jobs are asynchronous; they progress through states from Open to JobComplete or Failed.
layout: schema
name: Salesforce Bulk API 2.0 Job
properties_list:
- description: The unique identifier assigned to this Bulk API 2.0 job by Salesforce. Used in subsequent API calls to check status, upload data, and retrieve results.
  name: id
  type: string
- description: 'The data operation performed by this job. For ingest jobs: insert (create new records), update (modify existing records by ID), upsert (create or update based on external ID), delete (soft-delete reco'
  name: operation
  type: string
- description: The API name of the Salesforce SObject type being processed by this job (e.g., Account, Contact, Opportunity, MyCustomObject__c).
  name: object
  type: string
- description: 'The current lifecycle state of the job. Open: job is accepting data uploads. UploadComplete: all data has been uploaded and the job is queued for processing. InProgress: the job is actively processing'
  name: state
  type: string
- description: The date and time the job was created, in ISO 8601 format (e.g., 2024-01-15T10:30:00.000Z).
  name: createdDate
  type: string
- description: The date and time the job was last modified by any operation (including system updates), in ISO 8601 format. Updated each time the job state changes.
  name: systemModstamp
  type: string
- description: The total number of records that have been processed so far by this job, including both successful and failed records. Updated after processing completes for each batch internally.
  name: numberRecordsProcessed
  type: integer
- description: The number of records that failed to process due to errors (e.g., validation errors, duplicate rules, required field violations). These records are available in the failedResults endpoint.
  name: numberRecordsFailed
  type: integer
- description: The total time in milliseconds spent processing this job. Only available after the job reaches JobComplete or Failed state.
  name: totalProcessingTime
  type: integer
- description: A message describing the error that caused the job to fail. Only present when the job state is Failed. Describes the reason the entire job could not be processed (as opposed to individual record error
  name: errorMessage
  type: string
- description: The file format of the data uploaded to or returned from this job. Currently only CSV (comma-separated values) is supported by Bulk API 2.0.
  name: contentType
  type: string
- description: The line ending character sequence used in the CSV data for this job. LF uses Unix-style line endings (\n). CRLF uses Windows-style line endings (\r\n).
  name: lineEnding
  type: string
- description: The character used as the column delimiter in the CSV data for this job. COMMA is the default and most common. TAB, PIPE, SEMICOLON, CARET, and BACKQUOTE are alternatives for data that contains commas
  name: columnDelimiter
  type: string
- description: The API name of the external ID field used to match records for upsert operations. Only present for jobs with operation 'upsert'. The CSV data must include this field in every row.
  name: externalIdFieldName
  type: string
- description: The type of Bulk API job. V2Ingest indicates a Bulk API 2.0 ingest job. V2Query indicates a Bulk API 2.0 query job. Classic indicates a Bulk API 1.0 job.
  name: jobType
  type: string
- description: The 18-character Salesforce user ID of the user who created this job.
  name: createdById
  type: string
- description: The Salesforce API version used to create this job (e.g., 63.0).
  name: apiVersion
  type: number
- description: The concurrency mode for processing. Parallel mode processes batches simultaneously for better performance. Serial mode processes batches one at a time to avoid lock contention.
  name: concurrencyMode
  type: string
- description: The number of times Salesforce has retried processing this job after transient failures.
  name: retries
  type: integer
provider_name: Salesforce
provider_slug: salesforce
schema_file: json-schema/salesforce-bulk-job-schema.json
slug: salesforce-bulk-job
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
title: Salesforce Bulk API 2.0 Job
---
