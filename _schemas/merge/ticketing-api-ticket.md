---
description: A ticket or issue from a connected ticketing or project management system.
layout: schema
name: Ticket
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: remote_id
  type: string
- description: Ticket title or name.
  name: name
  type: string
- description: ''
  name: assignees
  type: array
- description: ''
  name: creator
  type: string
- description: ''
  name: due_date
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: priority
  type: string
- description: ''
  name: ticket_type
  type: string
- description: ''
  name: account
  type: string
- description: ''
  name: contact
  type: string
- description: ''
  name: parent_ticket
  type: string
- description: ''
  name: tags
  type: array
- description: ''
  name: completed_at
  type: string
- description: ''
  name: ticket_url
  type: string
- description: ''
  name: remote_was_deleted
  type: boolean
- description: ''
  name: created_at
  type: string
- description: ''
  name: modified_at
  type: string
provider_name: Merge
provider_slug: merge
schema_file: json-schema/ticketing-api-ticket-schema.json
slug: ticketing-api-ticket
tags:
- Integrations
- Platform
- Unified API
title: Ticket
---
