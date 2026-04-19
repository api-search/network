---
consumed_apis:
- crm-tickets
- conversations
- crm-contacts
- crm-associations
description: Unified workflow for service agents to manage support tickets, conversations, threads, messages, and CRM associations. Combines ticket management with conversation channels for complete customer service operations.
layout: capability
name: HubSpot Customer Service
operations:
- description: List tickets
  method: GET
  name: list-tickets
  path: /v1/tickets
- description: Create ticket
  method: POST
  name: create-ticket
  path: /v1/tickets
- description: Get ticket
  method: GET
  name: get-ticket
  path: /v1/tickets/{ticketId}
- description: Update ticket
  method: PATCH
  name: update-ticket
  path: /v1/tickets/{ticketId}
- description: Get contact
  method: GET
  name: get-contact
  path: /v1/contacts/{contactId}
personas: []
provider_name: HubSpot
provider_slug: hubspot
search_terms:
- look up a contact for ticket context
- associate a ticket with a contact or company
- archive a support ticket
- marketing
- search contacts
- list all support tickets
- service
- content
- operations
- update a support ticket
- conversations
- list tickets
- list associations
- search tickets
- create association
- get a support ticket by id
- get contact
- support tickets
- individual ticket
- customer service
- analytics
- update ticket
- crm
- marketing automation
- search contacts to find the customer
- search tickets with filters
- hubspot
- archive ticket
- list associations for a crm object
- sales
- commerce
- tickets
- create ticket
- email marketing
- support
- create a new support ticket
- get ticket
- contact lookup
slug: customer-service
tags:
- HubSpot
- Service
- Support
- Tickets
- Conversations
tools:
- description: List all support tickets
  hints:
    idempotent: true
    readOnly: true
  name: list-tickets
- description: Get a support ticket by ID
  hints:
    idempotent: true
    readOnly: true
  name: get-ticket
- description: Create a new support ticket
  hints:
    readOnly: false
  name: create-ticket
- description: Update a support ticket
  hints:
    idempotent: true
    readOnly: false
  name: update-ticket
- description: Archive a support ticket
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: archive-ticket
- description: Search tickets with filters
  hints:
    idempotent: true
    readOnly: true
  name: search-tickets
- description: Look up a contact for ticket context
  hints:
    idempotent: true
    readOnly: true
  name: get-contact
- description: Search contacts to find the customer
  hints:
    idempotent: true
    readOnly: true
  name: search-contacts
- description: List associations for a CRM object
  hints:
    idempotent: true
    readOnly: true
  name: list-associations
- description: Associate a ticket with a contact or company
  hints:
    idempotent: true
    readOnly: false
  name: create-association
---
