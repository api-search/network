---
description: Historical value of a property
layout: schema
name: PropertyHistory
properties_list:
- description: The historical value
  name: value
  type: string
- description: When the value was set
  name: timestamp
  type: string
- description: The source type that set this value
  name: sourceType
  type: string
- description: The source identifier
  name: sourceId
  type: string
- description: Human-readable source label
  name: sourceLabel
  type: string
- description: The user ID who made the change
  name: updatedByUserId
  type: integer
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-engagement-notes-property-history-schema.json
slug: hubspot-engagement-notes-property-history
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
title: PropertyHistory
---
