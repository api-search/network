---
description: Groups of organization members that gives permissions on specified repositories.
layout: schema
name: team-full
properties_list:
- description: Unique identifier of the team
  name: id
  type: integer
- description: ''
  name: node_id
  type: string
- description: URL for the team
  name: url
  type: string
- description: ''
  name: html_url
  type: string
- description: Name of the team
  name: name
  type: string
- description: ''
  name: slug
  type: string
- description: ''
  name: description
  type: string
- description: The level of privacy this team should have
  name: privacy
  type: string
- description: Permission that the team will have for its repositories
  name: permission
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
- description: ''
  name: members_count
  type: integer
- description: ''
  name: repos_count
  type: integer
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
- description: ''
  name: organization
  type: object
- description: Distinguished Name (DN) that team maps to within LDAP environment
  name: ldap_dn
  type: string
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-teams-team-full-schema.json
slug: github-teams-team-full
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: team-full
---
