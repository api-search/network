---
description: ''
layout: schema
name: TroubleTicketCreate
properties_list:
- description: Name of the trouble ticket, typically a short description of the issue
  name: name
  type: string
- description: A description of the issue
  name: description
  type: string
- description: 'The severity of the issue (must provide choice value only): - 1: Critical - 2: High - 3: Moderate - 4: Low - 5: Planning (Incident only)'
  name: severity
  type: string
- description: The current status of the trouble ticket (can provide choice label or value)
  name: status
  type: string
- description: The type of ticket to create
  name: ticketType
  type: string
- description: ''
  name: channel
  type: object
- description: List of work notes and comments to add to the ticket
  name: note
  type: array
- description: List of impacted assets, products, sold products, configuration items, or services
  name: relatedEntity
  type: array
- description: Details about contacts for the ticket
  name: relatedParty
  type: array
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/trouble-ticket-trouble-ticket-create-schema.json
slug: trouble-ticket-trouble-ticket-create
tags:
- Automation
- Cloud Services
- Digital Workflows
- Enterprise Platform
- IT Service Management
- ITSM
- Processes
- T1
- Workflow Automation
- Workflows
title: TroubleTicketCreate
---
