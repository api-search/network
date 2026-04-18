---
description: Request body for searching notes
layout: schema
name: NoteSearchRequest
properties_list:
- description: Filter groups for the search (OR logic between groups)
  name: filterGroups
  type: array
- description: Sort order for results
  name: sorts
  type: array
- description: Full-text search query
  name: query
  type: string
- description: Properties to return
  name: properties
  type: array
- description: Maximum results to return
  name: limit
  type: integer
- description: Pagination cursor
  name: after
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/engagement-notes-note-search-request-schema.json
slug: engagement-notes-note-search-request
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
title: NoteSearchRequest
---
