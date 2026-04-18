---
description: Detailed information about a Bulk API 2.0 query job, including its current state and processing statistics.
layout: schema
name: QueryJobInfo
properties_list:
- description: The unique identifier of the query job.
  name: id
  type: string
- description: The query operation being performed.
  name: operation
  type: string
- description: The primary SObject type in the SOQL query. Derived automatically from the query.
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
- description: The number of records returned by the query.
  name: numberRecordsProcessed
  type: integer
- description: Total processing time in milliseconds.
  name: totalProcessingTime
  type: integer
- description: Error message if the job reached the Failed state. Describes the reason for failure.
  name: errorMessage
  type: string
- description: The content type of the query results.
  name: contentType
  type: string
- description: The column delimiter used in the results CSV.
  name: columnDelimiter
  type: string
- description: The line ending used in the results CSV.
  name: lineEnding
  type: string
- description: The job type (V2Query for Bulk API 2.0 query jobs).
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
schema_file: json-schema/salesforce-bulk-2-query-job-info-schema.json
slug: salesforce-bulk-2-query-job-info
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
title: QueryJobInfo
---
