---
description: A Snowflake job service object.
layout: schema
name: JobService
properties_list:
- description: The current status of the service.
  name: status
  type: string
- description: Specifies the name of the compute pool in your account on which to run the service.
  name: compute_pool
  type: string
- description: Specifies the names of the external access integrations that allow your service to access external sites.
  name: external_access_integrations
  type: array
- description: Specifies a comment for the service.
  name: comment
  type: string
- description: True if the service is an async job service; false otherwise.
  name: is_async_job
  type: boolean
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/service-job-service-schema.json
slug: service-job-service
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: JobService
---
