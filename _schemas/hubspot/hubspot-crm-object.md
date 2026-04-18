---
description: Schema for a HubSpot CRM object record, applicable to contacts, companies, deals, tickets, and other CRM object types.
layout: schema
name: HubSpot CRM Object
properties_list:
- description: The unique identifier for the CRM object record assigned by HubSpot.
  name: id
  type: string
- description: The CRM object's properties as key-value pairs. Keys are property names and values are the property values as strings.
  name: properties
  type: object
- description: A map of property names to their historical values, including the current value and previous values with timestamps.
  name: propertiesWithHistory
  type: object
- description: The date and time the CRM object record was created in ISO 8601 format.
  name: createdAt
  type: string
- description: The date and time the CRM object record was last updated in ISO 8601 format.
  name: updatedAt
  type: string
- description: Whether the CRM object record has been archived (soft deleted). Archived records can be restored.
  name: archived
  type: boolean
- description: The date and time the CRM object record was archived, if applicable.
  name: archivedAt
  type: string
- description: Associations between this CRM object and other CRM objects, keyed by object type.
  name: associations
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-crm-object-schema.json
slug: hubspot-crm-object
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
title: HubSpot CRM Object
---
