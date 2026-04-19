---
description: StartExportTaskRequest schema from Amazon Application Discovery Service API
layout: schema
name: StartExportTaskRequest
properties_list:
- description: 'The file format for the returned export data. Default(s) are CSV. Note: The GRAPHML option has been deprecated.'
  name: exportDataFormat
  type: array
- description: If a filter is present, it selects the single agentId of the Application Discovery Agent for which data is exported.
  name: filters
  type: array
- description: The start timestamp for exported data from the single Application Discovery Agent selected in the filters.
  name: startTime
  type: string
- description: The end timestamp for exported data from the single Application Discovery Agent selected in the filters.
  name: endTime
  type: string
- description: Indicates the type of agent export.
  name: preferences
  type: object
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-start-export-task-request-schema.json
slug: application-discovery-service-start-export-task-request
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: StartExportTaskRequest
---
