---
description: DescribeContinuousExportsRequest schema from Amazon Application Discovery Service API
layout: schema
name: DescribeContinuousExportsRequest
properties_list:
- description: The unique IDs assigned to the exports.
  name: exportIds
  type: array
- description: A number between 1 and 100 specifying the maximum number of continuous export descriptions returned.
  name: maxResults
  type: integer
- description: The token from the previous call to DescribeExportTasks.
  name: nextToken
  type: string
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-describe-continuous-exports-request-schema.json
slug: application-discovery-service-describe-continuous-exports-request
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: DescribeContinuousExportsRequest
---
