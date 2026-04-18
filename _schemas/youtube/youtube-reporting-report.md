---
description: ''
layout: schema
name: Report
properties_list:
- description: The server-generated ID of the report.
  name: id
  type: string
- description: The ID of the job that created this report.
  name: jobId
  type: string
- description: The start of the time period that the report covers.
  name: startTime
  type: string
- description: The end of the time period that the report covers.
  name: endTime
  type: string
- description: The date and time when the report was created.
  name: createTime
  type: string
- description: The URL from which the report can be downloaded.
  name: downloadUrl
  type: string
- description: The date and time when the job creating this report will expire.
  name: jobExpireTime
  type: string
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-reporting-report-schema.json
slug: youtube-reporting-report
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: Report
---
