---
description: A HubSpot ticket record.
layout: schema
name: Ticket
properties_list:
- description: The unique identifier for the ticket.
  name: id
  type: string
- description: The ticket's properties as key-value pairs.
  name: properties
  type: object
- description: The date and time the ticket was created.
  name: createdAt
  type: string
- description: The date and time the ticket was last updated.
  name: updatedAt
  type: string
- description: Whether the ticket has been archived.
  name: archived
  type: boolean
- description: The ticket's associations with other CRM objects.
  name: associations
  type: object
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/crm-tickets-api-ticket-schema.json
slug: crm-tickets-api-ticket
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
title: Ticket
---
