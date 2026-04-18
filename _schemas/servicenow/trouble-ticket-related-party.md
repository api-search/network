---
description: ''
layout: schema
name: RelatedParty
properties_list:
- description: Sys_id of the related party
  name: id
  type: string
- description: Name of the related party
  name: name
  type: string
- description: 'Type of related party: - assigned_to: User assigned to work on the ticket - assignment_group: Group assigned to work on the ticket - customer: Company or account for the ticket - customer_contact: Cal'
  name: '@referredType'
  type: string
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/trouble-ticket-related-party-schema.json
slug: trouble-ticket-related-party
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
title: RelatedParty
---
