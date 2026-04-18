---
description: ''
layout: schema
name: VerifyResponse
properties_list:
- description: Whether the token was valid.
  name: success
  type: boolean
- description: Timestamp of the challenge.
  name: challenge_ts
  type: string
- description: Hostname for which the challenge was solved.
  name: hostname
  type: string
- description: Error codes if verification failed.
  name: error-codes
  type: array
- description: The action name from the widget.
  name: action
  type: string
- description: Custom data from the widget.
  name: cdata
  type: string
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-turnstile-verify-response-schema.json
slug: cloudflare-turnstile-verify-response
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
title: VerifyResponse
---
