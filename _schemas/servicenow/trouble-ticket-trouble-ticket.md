---
description: ''
layout: schema
name: TroubleTicket
properties_list:
- description: This value is always TroubleTicket
  name: '@type'
  type: string
- description: The sys_id of the case or incident record
  name: id
  type: string
- description: Relative link to the case or incident record
  name: href
  type: string
- description: The date that the case or incident record was created
  name: creationDate
  type: string
- description: The date the record was last updated
  name: lastUpdate
  type: string
- description: The name of the trouble ticket, typically a short description of the issue
  name: name
  type: string
- description: The description of the issue from the ticket
  name: description
  type: string
- description: The severity of the issue described by the trouble ticket
  name: severity
  type: string
- description: The current status of the trouble ticket
  name: status
  type: string
- description: The type of ticket
  name: ticketType
  type: string
- description: ''
  name: channel
  type: object
- description: A list of all comments on the ticket (excludes work notes)
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
schema_file: json-schema/trouble-ticket-trouble-ticket-schema.json
slug: trouble-ticket-trouble-ticket
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
title: TroubleTicket
---
