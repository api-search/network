---
description: StartImportTaskRequest schema from Amazon Application Discovery Service API
layout: schema
name: StartImportTaskRequest
properties_list:
- description: Optional. A unique token that you can provide to prevent the same import request from occurring more than once.
  name: clientRequestToken
  type: string
- description: A descriptive name for this request. You can use this name to filter future requests related to this import task, such as identifying applications and servers that were included in this import task.
  name: name
  type: string
- description: The URL for your import file that you've uploaded to Amazon S3.
  name: importUrl
  type: string
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-start-import-task-request-schema.json
slug: application-discovery-service-start-import-task-request
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: StartImportTaskRequest
---
