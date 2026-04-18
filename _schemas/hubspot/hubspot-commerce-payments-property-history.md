---
description: A historical property value
layout: schema
name: PropertyHistory
properties_list:
- description: The property value
  name: value
  type: string
- description: When this value was set
  name: timestamp
  type: string
- description: The source that set this value
  name: sourceType
  type: string
- description: The identifier of the source
  name: sourceId
  type: string
- description: A human-readable label for the source
  name: sourceLabel
  type: string
- description: The user ID that made the change
  name: updatedByUserId
  type: integer
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-commerce-payments-property-history-schema.json
slug: hubspot-commerce-payments-property-history
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
