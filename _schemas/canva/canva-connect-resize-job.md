---
description: A resize job for creating a resized copy of a design
layout: schema
name: ResizeJob
properties_list:
- description: The resize job ID
  name: id
  type: string
- description: The current status of the resize job
  name: status
  type: string
- description: The resize result (present when status is success)
  name: result
  type: object
- description: Error details (present when status is failed)
  name: error
  type: object
provider_name: Canva
provider_slug: canva
schema_file: json-schema/canva-connect-resize-job-schema.json
slug: canva-connect-resize-job
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
title: ResizeJob
---
