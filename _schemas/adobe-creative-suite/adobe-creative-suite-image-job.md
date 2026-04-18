---
description: Schema for asynchronous image processing jobs submitted to Adobe Photoshop and related Creative Suite image APIs. Covers the full lifecycle of a job from submission through completion or failure, including input references, output references, and error details.
layout: schema
name: Adobe Creative Suite Image Job
properties_list:
- description: Unique identifier assigned to the image processing job upon submission
  name: jobId
  type: string
- description: Current lifecycle status of the image processing job
  name: status
  type: string
- description: ISO 8601 timestamp indicating when the job was submitted for processing
  name: created
  type: string
- description: ISO 8601 timestamp indicating when the job record was last updated
  name: modified
  type: string
- description: Reference to the input file used for this image processing job
  name: input
  type: object
- description: Reference to the output file location for this image processing job
  name: output
  type: object
- description: List of output files produced when the job succeeds (for multi-output operations)
  name: outputs
  type: array
- description: List of errors encountered during job processing (populated when status is failed)
  name: errors
  type: array
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
schema_file: json-schema/adobe-creative-suite-image-job-schema.json
slug: adobe-creative-suite-image-job
tags:
- Creative
- Design
- Graphics
- Photography
- Video
title: Adobe Creative Suite Image Job
---
