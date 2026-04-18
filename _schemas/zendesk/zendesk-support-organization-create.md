---
description: Payload for creating a new organization.
layout: schema
name: OrganizationCreate
properties_list:
- description: The name of the organization.
  name: name
  type: string
- description: ''
  name: details
  type: string
- description: ''
  name: notes
  type: string
- description: ''
  name: domain_names
  type: array
- description: ''
  name: group_id
  type: integer
- description: ''
  name: shared_tickets
  type: boolean
- description: ''
  name: shared_comments
  type: boolean
- description: ''
  name: external_id
  type: string
- description: ''
  name: tags
  type: array
- description: ''
  name: organization_fields
  type: object
provider_name: Zendesk
provider_slug: zendesk
schema_file: json-schema/zendesk-support-organization-create-schema.json
slug: zendesk-support-organization-create
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
title: OrganizationCreate
---
