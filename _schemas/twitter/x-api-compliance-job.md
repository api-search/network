---
description: ComplianceJob schema from X API v2
layout: schema
name: ComplianceJob
properties_list:
- description: Creation time of the compliance job.
  name: created_at
  type: string
- description: Expiration time of the download URL.
  name: download_expires_at
  type: string
- description: URL from which the user will retrieve their compliance results.
  name: download_url
  type: string
- description: Compliance Job ID.
  name: id
  type: string
- description: User-provided name for a compliance job.
  name: name
  type: string
- description: Status of a compliance job.
  name: status
  type: string
- description: Type of compliance job to list.
  name: type
  type: string
- description: Expiration time of the upload URL.
  name: upload_expires_at
  type: string
- description: URL to which the user will upload their Tweet or user IDs.
  name: upload_url
  type: string
provider_name: X (Twitter)
provider_slug: twitter
schema_file: json-schema/x-api-compliance-job-schema.json
slug: x-api-compliance-job
tags:
- Social Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
title: ComplianceJob
---
