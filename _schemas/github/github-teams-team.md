---
description: Groups of organization members that gives permissions on specified repositories.
layout: schema
name: team
properties_list:
- description: ''
  name: id
  type: integer
- description: ''
  name: node_id
  type: string
- description: ''
  name: name
  type: string
- description: ''
  name: slug
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: privacy
  type: string
- description: ''
  name: permission
  type: string
- description: ''
  name: permissions
  type: object
- description: ''
  name: url
  type: string
- description: ''
  name: html_url
  type: string
- description: ''
  name: members_url
  type: string
- description: ''
  name: repositories_url
  type: string
- description: ''
  name: parent
  type: object
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-teams-team-schema.json
slug: github-teams-team
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: team
---
