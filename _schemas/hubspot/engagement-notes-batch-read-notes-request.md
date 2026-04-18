---
description: Request body for batch reading notes
layout: schema
name: BatchReadNotesRequest
properties_list:
- description: Array of note identifiers
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
schema_file: json-schema/engagement-notes-batch-read-notes-request-schema.json
slug: engagement-notes-batch-read-notes-request
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
title: BatchReadNotesRequest
---
