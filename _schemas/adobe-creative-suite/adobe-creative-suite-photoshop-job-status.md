---
description: Current status and result of an asynchronous job
layout: schema
name: JobStatus
properties_list:
- description: Unique identifier of the job
  name: jobId
  type: string
- description: Current job status
  name: status
  type: string
- description: ISO 8601 timestamp when the job was created
  name: created
  type: string
- description: ISO 8601 timestamp when the job was last modified
  name: modified
  type: string
- description: List of output files produced by a successful job
  name: outputs
  type: array
- description: List of errors if the job failed
  name: errors
  type: array
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-photoshop-job-status-schema.json
slug: adobe-creative-suite-photoshop-job-status
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: JobStatus
---
