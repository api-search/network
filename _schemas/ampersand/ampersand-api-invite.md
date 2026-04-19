---
description: Invite schema from Ampersand API
layout: schema
name: Invite
properties_list:
- description: The invite ID.
  name: id
  type: string
- description: The email address of the person invited.
  name: invitedEmail
  type: string
- description: The type of entity that the person is invited to.
  name: parentType
  type: string
- description: The ID of the parent (e.g. org ID).
  name: parentId
  type: string
- description: The status of the invite.
  name: status
  type: string
- description: The time the invite was created.
  name: createTime
  type: string
- description: The time the invite was updated.
  name: updateTime
  type: string
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-invite-schema.json
slug: ampersand-api-invite
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: Invite
---
