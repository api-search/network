---
description: ''
layout: schema
name: Note
properties_list:
- description: The type of note (always 'comments' in responses)
  name: '@type'
  type: string
- description: The comment text
  name: text
  type: string
- description: The date the comment was created
  name: date
  type: string
- description: The name of the user who wrote the comment
  name: author
  type: string
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/trouble-ticket-note-schema.json
slug: trouble-ticket-note
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
title: Note
---
