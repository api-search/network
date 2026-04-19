---
description: ContinuousExportDescription schema from Amazon Application Discovery Service API
layout: schema
name: ContinuousExportDescription
properties_list:
- description: The unique ID assigned to this export.
  name: exportId
  type: string
- description: Describes the status of the export. Can be one of the following values — START_IN_PROGRESS, START_FAILED, ACTIVE, ERROR, STOP_IN_PROGRESS, STOP_FAILED, INACTIVE.
  name: status
  type: string
- description: Contains information about any errors that have occurred.
  name: statusDetail
  type: string
- description: The name of the s3 bucket where the export data parquet files are stored.
  name: s3Bucket
  type: string
- description: The timestamp representing when the continuous export was started.
  name: startTime
  type: string
- description: The timestamp representing when the continuous export was stopped.
  name: stopTime
  type: string
- description: The type of data collector used to gather this data.
  name: dataSource
  type: string
- description: An object which describes how the data is stored.
  name: schemaStorageConfig
  type: object
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-continuous-export-description-schema.json
slug: application-discovery-service-continuous-export-description
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: ContinuousExportDescription
---
