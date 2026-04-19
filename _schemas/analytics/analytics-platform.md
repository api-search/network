---
description: Schema describing an analytics platform, SDK, or tool in the analytics ecosystem
layout: schema
name: Analytics Platform
properties_list:
- description: Name of the analytics platform
  name: name
  type: string
- description: URL-friendly identifier
  name: slug
  type: string
- description: Description of the platform's capabilities
  name: description
  type: string
- description: Primary category of analytics
  name: category
  type: string
- description: Deployment model
  name: deployment
  type: string
- description: License type (MIT, Apache-2.0, Commercial, etc.)
  name: license
  type: string
- description: ''
  name: website
  type: string
- description: Link to API reference documentation
  name: apiReference
  type: string
- description: Available SDKs and client libraries
  name: sdks
  type: array
- description: Data collection capabilities
  name: dataCollection
  type: object
- description: Privacy and compliance features
  name: privacy
  type: object
- description: Available integrations and destinations
  name: integrations
  type: array
- description: ''
  name: pricing
  type: object
- description: ''
  name: tags
  type: array
provider_name: Analytics
provider_slug: analytics
schema_file: json-schema/analytics-platform-schema.json
slug: analytics-platform
tags:
- Analytics
- Business Intelligence
- Customer Data Platform
- Data Pipeline
- Event Tracking
- Mobile Analytics
- Observability
- Product Analytics
- Real-Time Analytics
- Web Analytics
title: Analytics Platform
---
