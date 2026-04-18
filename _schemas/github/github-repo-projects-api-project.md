---
description: Projects are a way to organize columns and cards of work.
layout: schema
name: project
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
- description: Name of the project
  name: name
  type: string
- description: Body of the project
  name: body
  type: string
- description: ''
  name: number
  type: integer
- description: State of the project; either 'open' or 'closed'
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
- description: The baseline permission that all organization members have on this project. Only present if owner is an organization.
  name: organization_permission
  type: string
- description: Whether or not this project can be seen by everyone. Only present if owner is an organization.
  name: private
  type: boolean
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-repo-projects-api-project-schema.json
slug: github-repo-projects-api-project
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: project
---
