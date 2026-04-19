---
description: An export job for converting a design to a downloadable format
layout: schema
name: ExportJob
properties_list:
- description: The export job ID
  name: id
  type: string
- description: The current status of the export job
  name: status
  type: string
- description: Download URLs for the exported files (valid for 24 hours). Present only when status is success.
  name: urls
  type: array
provider_name: Canva
provider_slug: canva
schema_file: json-schema/canva-connect-export-job-schema.json
slug: canva-connect-export-job
tags:
- Apps
- Automation
- Brand Management
- Collaboration
- Design
- Graphics
- Marketing
- Print
- Templates
- Visual Content
title: ExportJob
---
