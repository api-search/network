---
description: A team's access to a project.
layout: schema
name: team-project
properties_list:
- description: ''
  name: owner_url
  type: string
- description: ''
  name: url
  type: string
- description: ''
  name: html_url
  type: string
- description: ''
  name: columns_url
  type: string
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
  name: body
  type: string
- description: ''
  name: number
  type: integer
- description: ''
  name: state
  type: string
- description: ''
  name: creator
  type: object
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
- description: The organization permission for this project. Only present when owner is an organization.
  name: organization_permission
  type: string
- description: Whether the project is private or not. Only present when owner is an organization.
  name: private
  type: boolean
- description: ''
  name: permissions
  type: object
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-projects-team-project-schema.json
slug: github-projects-team-project
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: team-project
---
