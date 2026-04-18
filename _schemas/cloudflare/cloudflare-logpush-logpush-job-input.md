---
description: ''
layout: schema
name: LogpushJobInput
properties_list:
- description: Name for the job.
  name: name
  type: string
- description: Whether the job is active.
  name: enabled
  type: boolean
- description: The log dataset to push.
  name: dataset
  type: string
- description: Destination URI.
  name: destination_conf
  type: string
- description: Options for log fields and formatting.
  name: logpull_options
  type: string
- description: ''
  name: frequency
  type: string
- description: JSON filter expression to limit logs pushed.
  name: filter
  type: string
- description: The ownership challenge token.
  name: ownership_challenge
  type: string
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-logpush-logpush-job-input-schema.json
slug: cloudflare-logpush-logpush-job-input
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
title: LogpushJobInput
---
