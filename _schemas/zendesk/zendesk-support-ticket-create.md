---
description: Payload for creating a new ticket.
layout: schema
name: TicketCreate
properties_list:
- description: The subject of the ticket.
  name: subject
  type: string
- description: The initial comment (description) of the ticket.
  name: comment
  type: object
- description: The ID of the requester.
  name: requester_id
  type: integer
- description: Requester details for creating a new user inline. Use either requester_id or requester, not both.
  name: requester
  type: object
- description: The ID of the submitter.
  name: submitter_id
  type: integer
- description: The ID of the assigned agent.
  name: assignee_id
  type: integer
- description: The ID of the assigned group.
  name: group_id
  type: integer
- description: ''
  name: organization_id
  type: integer
- description: ''
  name: type
  type: string
- description: ''
  name: priority
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: tags
  type: array
- description: ''
  name: external_id
  type: string
- description: ''
  name: custom_fields
  type: array
- description: ''
  name: due_at
  type: string
- description: ''
  name: ticket_form_id
  type: integer
- description: ''
  name: brand_id
  type: integer
- description: ''
  name: collaborator_ids
  type: array
- description: ''
  name: email_cc_ids
  type: array
- description: ''
  name: problem_id
  type: integer
provider_name: Zendesk
provider_slug: zendesk
schema_file: json-schema/zendesk-support-ticket-create-schema.json
slug: zendesk-support-ticket-create
tags:
- Chat
- CRM
- Help Center
- Sell
- Support
- T1
- Talk
- Ticketing
- Tickets
title: TicketCreate
---
