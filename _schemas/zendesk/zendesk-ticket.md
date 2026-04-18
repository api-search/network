---
description: A Zendesk Support ticket representing a customer service request. Tickets are the core entity in Zendesk Support, capturing the communication between a customer and support agents. Each ticket has a lifecycle from creation through resolution, with statuses, priorities, assignees, and a full audit trail of changes and comments.
layout: schema
name: Zendesk Ticket
properties_list:
- description: Automatically assigned unique identifier for the ticket.
  name: id
  type: integer
- description: The API URL of the ticket resource.
  name: url
  type: string
- description: An optional ID from an external system used to link the ticket to records outside Zendesk.
  name: external_id
  type:
  - string
  - 'null'
- description: The classification of the ticket. 'problem' tickets can have linked 'incident' tickets. 'task' tickets support due dates.
  name: type
  type:
  - string
  - 'null'
- description: The subject line of the ticket, typically a brief summary of the issue.
  name: subject
  type: string
- description: The original subject as entered by the requester, before any processing by Zendesk.
  name: raw_subject
  type: string
- description: The first comment on the ticket, set at creation time. Read-only after the ticket is created.
  name: description
  type: string
- description: The urgency level of the ticket.
  name: priority
  type:
  - string
  - 'null'
- description: The current state of the ticket in its lifecycle.
  name: status
  type: string
- description: The original recipient email address of the ticket.
  name: recipient
  type:
  - string
  - 'null'
- description: The ID of the user who requested the ticket (the customer).
  name: requester_id
  type: integer
- description: The ID of the user who submitted the ticket. Can differ from the requester when an agent creates a ticket on behalf of a customer.
  name: submitter_id
  type: integer
- description: The ID of the agent currently assigned to the ticket.
  name: assignee_id
  type:
  - integer
  - 'null'
- description: The ID of the organization associated with the ticket.
  name: organization_id
  type:
  - integer
  - 'null'
- description: The ID of the agent group assigned to the ticket.
  name: group_id
  type:
  - integer
  - 'null'
- description: IDs of users currently CC'd on the ticket.
  name: collaborator_ids
  type: array
- description: IDs of agents currently following the ticket for internal notifications.
  name: follower_ids
  type: array
- description: IDs of agents or end users currently CC'd on the ticket via email.
  name: email_cc_ids
  type: array
- description: The ID of the associated community forum topic, if the ticket originated from a forum post.
  name: forum_topic_id
  type:
  - integer
  - 'null'
- description: For incident tickets, the ID of the problem ticket this incident is linked to.
  name: problem_id
  type:
  - integer
  - 'null'
- description: Whether this problem ticket has associated incident tickets.
  name: has_incidents
  type: boolean
- description: Whether the ticket has any public-facing comments.
  name: is_public
  type: boolean
- description: The due date for task-type tickets, in ISO 8601 format.
  name: due_at
  type:
  - string
  - 'null'
- description: Tags applied to the ticket for categorization and routing.
  name: tags
  type: array
- description: Custom field values set on the ticket.
  name: custom_fields
  type: array
- description: The satisfaction rating left by the customer, if any.
  name: satisfaction_rating
  type:
  - object
  - 'null'
- description: IDs of sharing agreements used for the ticket.
  name: sharing_agreement_ids
  type: array
- description: The ID of the custom ticket status, if custom statuses are enabled.
  name: custom_status_id
  type:
  - integer
  - 'null'
- description: IDs of follow-up tickets created from this closed ticket.
  name: followup_ids
  type: array
- description: The ID of the ticket form used for this ticket.
  name: ticket_form_id
  type:
  - integer
  - 'null'
- description: The ID of the brand associated with this ticket.
  name: brand_id
  type:
  - integer
  - 'null'
- description: Whether channelback is enabled for this ticket.
  name: allow_channelback
  type: boolean
- description: Whether the ticket allows file attachments.
  name: allow_attachments
  type: boolean
- description: Whether the ticket originated from a messaging channel.
  name: from_messaging_channel
  type: boolean
- description: How the ticket was created (e.g., web, email, API, chat).
  name: via
  type: object
- description: When the ticket was created, in ISO 8601 format.
  name: created_at
  type: string
- description: When the ticket was last updated, in ISO 8601 format.
  name: updated_at
  type: string
provider_name: Zendesk
provider_slug: zendesk
schema_file: json-schema/zendesk-ticket-schema.json
slug: zendesk-ticket
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
title: Zendesk Ticket
---
