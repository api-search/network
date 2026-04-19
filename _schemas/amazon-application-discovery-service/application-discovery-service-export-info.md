---
description: ExportInfo schema from Amazon Application Discovery Service API
layout: schema
name: ExportInfo
properties_list:
- description: A unique identifier used to query the status of an export request.
  name: exportId
  type: string
- description: The status of the data export job.
  name: exportStatus
  type: string
- description: A status message provided for API callers.
  name: statusMessage
  type: string
- description: A URL for an Amazon S3 bucket where you can review the exported data.
  name: configurationsDownloadUrl
  type: string
- description: The time that the data export was initiated.
  name: exportRequestTime
  type: string
- description: If true, the export of agent information exceeded the size limit for a single export, and the exported data is incomplete.
  name: isTruncated
  type: boolean
- description: The value of startTime parameter in the StartExportTask request.
  name: requestedStartTime
  type: string
- description: The endTime used in the StartExportTask request. If no endTime was requested, this result does not appear in ExportInfo.
  name: requestedEndTime
  type: string
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-export-info-schema.json
slug: application-discovery-service-export-info
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: ExportInfo
---
