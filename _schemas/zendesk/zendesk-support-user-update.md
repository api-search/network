---
description: Payload for updating an existing user.
layout: schema
name: UserUpdate
properties_list:
- description: ''
  name: name
  type: string
- description: ''
  name: email
  type: string
- description: ''
  name: phone
  type: string
- description: ''
  name: role
  type: string
- description: ''
  name: custom_role_id
  type: integer
- description: ''
  name: organization_id
  type: integer
- description: ''
  name: external_id
  type: string
- description: ''
  name: tags
  type: array
- description: ''
  name: locale_id
  type: integer
- description: ''
  name: time_zone
  type: string
- description: ''
  name: details
  type: string
- description: ''
  name: notes
  type: string
- description: ''
  name: alias
  type: string
- description: ''
  name: signature
  type: string
- description: ''
  name: suspended
  type: boolean
- description: ''
  name: user_fields
  type: object
provider_name: Zendesk
provider_slug: zendesk
schema_file: json-schema/zendesk-support-user-update-schema.json
slug: zendesk-support-user-update
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
title: UserUpdate
---
