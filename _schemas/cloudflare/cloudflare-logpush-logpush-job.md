---
description: ''
layout: schema
name: LogpushJob
properties_list:
- description: The unique identifier of the job.
  name: id
  type: integer
- description: A human-readable name for the job.
  name: name
  type: string
- description: Whether the job is active.
  name: enabled
  type: boolean
- description: The log dataset.
  name: dataset
  type: string
- description: The destination configuration URI.
  name: destination_conf
  type: string
- description: Logpull options specifying fields, timestamps, and sample rate.
  name: logpull_options
  type: string
- description: Log push frequency.
  name: frequency
  type: string
- description: Timestamp of the last successful push.
  name: last_complete
  type: string
- description: Timestamp of the last error.
  name: last_error
  type: string
- description: Last error message.
  name: error_message
  type: string
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-logpush-logpush-job-schema.json
slug: cloudflare-logpush-logpush-job
tags:
- AI Gateway
- API Gateway
- Artificial Intelligence
- CDN
- Cloud
- Containers
- DDoS Protection
- DNS
- Edge
- Edge Computing
- Object Storage
- Platform
- Real-Time Communication
- Security
- Serverless
- Web Performance
title: LogpushJob
---
