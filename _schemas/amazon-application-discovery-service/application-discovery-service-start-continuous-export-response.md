---
description: StartContinuousExportResponse schema from Amazon Application Discovery Service API
layout: schema
name: StartContinuousExportResponse
properties_list:
- description: The unique ID assigned to this export.
  name: exportId
  type: string
- description: The name of the s3 bucket where the export data parquet files are stored.
  name: s3Bucket
  type: string
- description: The timestamp representing when the continuous export was started.
  name: startTime
  type: string
- description: The type of data collector used to gather this data.
  name: dataSource
  type: string
- description: A dictionary which describes how the data is stored.
  name: schemaStorageConfig
  type: object
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-start-continuous-export-response-schema.json
slug: application-discovery-service-start-continuous-export-response
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: StartContinuousExportResponse
---
