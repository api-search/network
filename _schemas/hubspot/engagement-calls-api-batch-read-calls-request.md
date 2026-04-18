---
description: Request body for batch reading calls
layout: schema
name: BatchReadCallsRequest
properties_list:
- description: Array of call identifiers
  name: inputs
  type: array
- description: Properties to return
  name: properties
  type: array
- description: Properties to return with history
  name: propertiesWithHistory
  type: array
- description: The property to use as the identifier
  name: idProperty
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/engagement-calls-api-batch-read-calls-request-schema.json
slug: engagement-calls-api-batch-read-calls-request
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
title: BatchReadCallsRequest
---
