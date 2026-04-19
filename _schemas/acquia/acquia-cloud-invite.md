---
description: Details an invite.
layout: schema
name: Invite
properties_list:
- description: The unique identifier of the Invite.
  name: uuid
  type: string
- description: The invitee email address.
  name: email
  type: string
- description: The invite creation time.
  name: created_at
  type: string
- description: The invite token.
  name: token
  type: string
- description: ''
  name: flags
  type: object
- description: ''
  name: author
  type: object
- description: ''
  name: organization
  type: object
- description: ''
  name: team
  type: object
- description: List of applications the invite will grant the invitee.
  name: applications
  type: array
- description: List of roles the invite will grant the invitee.
  name: roles
  type: array
- description: ''
  name: _links
  type: object
provider_name: Acquia
provider_slug: acquia
schema_file: json-schema/acquia-cloud-invite-schema.json
slug: acquia-cloud-invite
tags:
- Content
- Experience
title: Invite
---
