---
description: Allianz webhook implementation standard definition
layout: schema
name: WebhookGuideline
properties_list:
- description: Unique identifier for the webhook guideline
  name: guideline_id
  type: string
- description: Name of the guideline
  name: name
  type: string
- description: Version of the guideline
  name: version
  type: string
- description: Supported webhook notification types
  name: notification_types
  type: array
- description: Security requirements for webhook endpoints
  name: security_requirements
  type: array
provider_name: Allianz Technology Standards
provider_slug: allianz-technology-standards
schema_file: json-schema/tech-standards-webhook-guideline-schema.json
slug: tech-standards-webhook-guideline
tags:
- Best Practices
- Enterprise Architecture
- Guidelines
- Software Development
- Technology Standards
- API Design
- OpenAPI
title: WebhookGuideline
---
