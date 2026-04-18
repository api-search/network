---
description: Represents a note engagement in the CRM
layout: schema
name: Note
properties_list:
- description: The unique identifier for the note
  name: id
  type: string
- description: The note properties
  name: properties
  type: object
- description: Properties with their change history
  name: propertiesWithHistory
  type: object
- description: When the note was created
  name: createdAt
  type: string
- description: When the note was last updated
  name: updatedAt
  type: string
- description: Whether the note is archived
  name: archived
  type: boolean
- description: When the note was archived (if archived)
  name: archivedAt
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/engagement-notes-note-schema.json
slug: engagement-notes-note
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
title: Note
---
