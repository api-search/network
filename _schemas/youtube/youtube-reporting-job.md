---
description: ''
layout: schema
name: Job
properties_list:
- description: The server-generated ID of the job.
  name: id
  type: string
- description: The type of reports that the job creates.
  name: reportTypeId
  type: string
- description: The name of the job. Max length is 100 characters.
  name: name
  type: string
- description: The date and time when the job was created.
  name: createTime
  type: string
- description: The date and time when the job will expire.
  name: expireTime
  type: string
- description: Whether the job is system-managed.
  name: systemManaged
  type: boolean
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-reporting-job-schema.json
slug: youtube-reporting-job
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: Job
---
