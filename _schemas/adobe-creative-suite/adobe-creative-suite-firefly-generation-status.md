---
description: Current status and results of a Firefly generation job
layout: schema
name: GenerationStatus
properties_list:
- description: Unique identifier of the generation job
  name: jobId
  type: string
- description: Current status of the generation job
  name: status
  type: string
- description: ISO 8601 timestamp when the job was created
  name: created
  type: string
- description: ISO 8601 timestamp when the job was last modified
  name: modified
  type: string
- description: Generated output images or videos (present on success)
  name: outputs
  type: array
- description: Errors encountered during generation (present on failure)
  name: errors
  type: array
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-firefly-generation-status-schema.json
slug: adobe-creative-suite-firefly-generation-status
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: GenerationStatus
---
