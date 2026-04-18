---
description: Reference to an output file location in cloud storage
layout: schema
name: JobOutput
properties_list:
- description: URL or path where the output file will be stored
  name: href
  type: string
- description: Cloud storage provider type
  name: storage
  type: string
- description: MIME type of the output file
  name: type
  type: string
- description: Output width in pixels
  name: width
  type: integer
- description: Output height in pixels
  name: height
  type: integer
- description: Whether to overwrite the output file if it already exists
  name: overwrite
  type: boolean
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-photoshop-job-output-schema.json
slug: adobe-creative-suite-photoshop-job-output
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: JobOutput
---
