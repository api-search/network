---
description: DescribeExportTasksRequest schema from Amazon Application Discovery Service API
layout: schema
name: DescribeExportTasksRequest
properties_list:
- description: One or more unique identifiers used to query the status of an export request.
  name: exportIds
  type: array
- description: One or more filters.
  name: filters
  type: array
- description: The maximum number of volume results returned by DescribeExportTasks in paginated output.
  name: maxResults
  type: integer
- description: The nextToken value returned from a previous paginated DescribeExportTasks request.
  name: nextToken
  type: string
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-describe-export-tasks-request-schema.json
slug: application-discovery-service-describe-export-tasks-request
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: DescribeExportTasksRequest
---
