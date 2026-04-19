---
description: ''
layout: schema
name: IngestionJob
properties_list:
- description: Indicate if data described in source uri shall be deleted after ingestion. Source uri must be a cloud storage uri. If deletion failed, ingestion status is set to `FAILED`.
  name: deleteOrigin
  type: boolean
- description: Indicate if data described in source uri shall be copied for archive after ingestion. If copy failed, ingestion status is set to `FAILED`.
  name: nativeCopy
  type: boolean
- description: Uri of the resource to ingest. The uri must point to the main file of the resource.
  name: sourceUri
  type: string
- description: Type of data to ingest
  name: type
  type: string
- description: ''
  name: workspace
  type: object
provider_name: Airbus OneAtlas
provider_slug: airbus-oneatlas
schema_file: json-schema/oneatlas-ingestion-job-schema.json
slug: oneatlas-ingestion-job
tags:
- Imagery
- Satellites
title: IngestionJob
---
