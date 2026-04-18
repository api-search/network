---
channels:
- description: Channel for receiving notifications when a new ticket is created in Zendesk Support.
  name: ticketCreated
- description: Channel for receiving notifications when a ticket is updated, including status changes, reassignments, and new comments.
  name: ticketUpdated
- description: Channel for receiving notifications when a ticket is solved by an agent or automation.
  name: ticketSolved
- description: Channel for receiving notifications when a new user is created in Zendesk.
  name: userCreated
- description: Channel for receiving notifications when a user is updated.
  name: userUpdated
- description: Channel for receiving notifications when a new organization is created.
  name: organizationCreated
- description: Channel for receiving notifications when an organization is updated.
  name: organizationUpdated
- description: Channel for receiving notifications when a customer submits a satisfaction rating on a ticket.
  name: satisfactionRatingCreated
description: Zendesk Webhooks allow you to receive real-time HTTP notifications when events occur in your Zendesk account. Webhooks are the modern replacement for legacy targets and support event types for tickets, users, organizations, and messaging. When an event fires, Zendesk sends an HTTP POST request with a JSON payload to your configured endpoint URL. Webhooks can be connected to triggers, automations, and other Zendesk business rules.
layout: asyncapi
messages:
- description: ''
  name: TicketEvent
  summary: A webhook payload sent when a ticket-related event occurs in Zendesk. The payload contents are determined by the webhook's configured body template, which can include Zendesk placeholders for ticket, user, and organization data.
  title: Ticket Event
- description: ''
  name: UserEvent
  summary: A webhook payload sent when a user-related event occurs in Zendesk.
  title: User Event
- description: ''
  name: OrganizationEvent
  summary: A webhook payload sent when an organization-related event occurs in Zendesk.
  title: Organization Event
- description: ''
  name: SatisfactionRatingEvent
  summary: A webhook payload sent when a satisfaction rating is submitted by a customer.
  title: Satisfaction Rating Event
name: Zendesk Webhooks
provider_name: Zendesk
provider_slug: zendesk
servers:
- description: Your webhook endpoint that receives HTTP POST requests from Zendesk. You configure this URL when creating a webhook in Zendesk.
  name: zendeskWebhook
  protocol: https
  url: ''
slug: zendesk-webhooks-asyncapi
spec_file: asyncapi/zendesk-webhooks-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/asyncapi/zendesk-webhooks-asyncapi.yml
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
- AsyncAPI
- Webhooks
- Events
version: 1.0.0
---
