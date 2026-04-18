---
description: ''
layout: schema
name: Project
properties_list:
- description: The unique identifier of the project.
  name: id
  type: string
- description: The name of the project.
  name: name
  type: string
- description: The subdomain for the project.
  name: subdomain
  type: string
- description: Custom domains attached to the project.
  name: domains
  type: array
- description: The production branch name.
  name: production_branch
  type: string
- description: When the project was created.
  name: created_on
  type: string
- description: ''
  name: build_config
  type: object
provider_name: Cloudflare
provider_slug: cloudflare
schema_file: json-schema/cloudflare-pages-project-schema.json
slug: cloudflare-pages-project
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
title: Project
---
