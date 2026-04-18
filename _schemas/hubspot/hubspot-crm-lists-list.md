---
description: A HubSpot CRM list.
layout: schema
name: List
properties_list:
- description: The unique identifier for the list.
  name: listId
  type: string
- description: The name of the list.
  name: name
  type: string
- description: Whether the list is static (manually managed) or dynamic (filter-based).
  name: listType
  type: string
- description: The object type the list contains (e.g., 0-1 for contacts).
  name: objectTypeId
  type: string
- description: The current processing status of the list.
  name: processingStatus
  type: string
- description: The date and time the list was created.
  name: createdAt
  type: string
- description: The date and time the list was last updated.
  name: updatedAt
  type: string
- description: The filter definition for dynamic lists.
  name: filterBranch
  type: object
- description: The current number of members in the list.
  name: memberCount
  type: integer
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-crm-lists-list-schema.json
slug: hubspot-crm-lists-list
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
title: List
---
