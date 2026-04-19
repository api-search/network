---
description: A job queue within a render farm that organizes and schedules rendering jobs.
layout: schema
name: Queue
properties_list:
- description: The unique identifier of the queue
  name: queueId
  type: string
- description: ''
  name: farmId
  type: string
- description: ''
  name: displayName
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: createdAt
  type: string
provider_name: Amazon Deadline Cloud
provider_slug: amazon-deadline-cloud
schema_file: json-schema/queue-schema.json
slug: queue
tags:
- AWS
- Compute
- Media
- Rendering
- Visual Effects
title: Queue
---
