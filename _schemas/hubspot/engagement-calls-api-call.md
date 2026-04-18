---
description: Represents a call engagement in the CRM
layout: schema
name: Call
properties_list:
- description: The unique identifier for the call
  name: id
  type: string
- description: The call properties
  name: properties
  type: object
- description: Properties with their change history
  name: propertiesWithHistory
  type: object
- description: When the call was created
  name: createdAt
  type: string
- description: When the call was last updated
  name: updatedAt
  type: string
- description: Whether the call is archived
  name: archived
  type: boolean
- description: When the call was archived (if archived)
  name: archivedAt
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/engagement-calls-api-call-schema.json
slug: engagement-calls-api-call
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
title: Call
---
