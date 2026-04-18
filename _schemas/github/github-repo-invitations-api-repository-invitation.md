---
description: Repository invitations let you manage who you collaborate with.
layout: schema
name: repository-invitation
properties_list:
- description: Unique identifier of the repository invitation.
  name: id
  type: integer
- description: ''
  name: repository
  type: object
- description: ''
  name: invitee
  type: object
- description: ''
  name: inviter
  type: object
- description: The permission associated with the invitation.
  name: permissions
  type: string
- description: ''
  name: created_at
  type: string
- description: Whether or not the invitation has expired
  name: expired
  type: boolean
- description: URL for the repository invitation
  name: url
  type: string
- description: ''
  name: html_url
  type: string
- description: ''
  name: node_id
  type: string
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-repo-invitations-api-repository-invitation-schema.json
slug: github-repo-invitations-api-repository-invitation
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: repository-invitation
---
