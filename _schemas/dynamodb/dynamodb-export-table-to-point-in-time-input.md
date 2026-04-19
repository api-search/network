---
description: ''
layout: schema
name: ExportTableToPointInTimeInput
properties_list:
- description: ARN of the table to export
  name: TableArn
  type: string
- description: Time in the past from which to export table data
  name: ExportTime
  type: string
- description: Idempotency token
  name: ClientToken
  type: string
- description: Name of the S3 bucket to export to
  name: S3Bucket
  type: string
- description: Account ID of the S3 bucket owner
  name: S3BucketOwner
  type: string
- description: S3 key prefix for the export
  name: S3Prefix
  type: string
- description: ''
  name: S3SseAlgorithm
  type: string
- description: ''
  name: S3SseKmsKeyId
  type: string
- description: ''
  name: ExportFormat
  type: string
provider_name: Amazon DynamoDB
provider_slug: dynamodb
schema_file: json-schema/dynamodb-export-table-to-point-in-time-input-schema.json
slug: dynamodb-export-table-to-point-in-time-input
tags:
- AWS
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- NoSQL
- Serverless
title: ExportTableToPointInTimeInput
---
