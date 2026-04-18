---
description: ''
layout: schema
name: Queue
properties_list:
- description: The unique identifier of the queue.
  name: queue_id
  type: string
- description: The name of the queue.
  name: queue_name
  type: string
- description: When the queue was created.
  name: created_on
  type: string
- description: When the queue was last modified.
  name: modified_on
  type: string
- description: Number of producers attached.
  name: producers_total_count
  type: integer
- description: Number of consumers attached.
  name: consumers_total_count
  type: integer
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-queues-queue-schema.json
slug: cloudflare-queues-queue
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
title: Queue
---
