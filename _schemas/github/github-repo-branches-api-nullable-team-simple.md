---
description: Groups of organization members that gives permissions on specified repositories.
layout: schema
name: nullable-team-simple
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
  name: members_url
  type: string
- description: Name of the team
  name: name
  type: string
- description: Description of the team
  name: description
  type: string
- description: Permission that the team will have for its repositories
  name: permission
  type: string
- description: The level of privacy this team should have
  name: privacy
  type: string
- description: ''
  name: html_url
  type: string
- description: ''
  name: repositories_url
  type: string
- description: ''
  name: slug
  type: string
- description: Distinguished Name (DN) that team maps to within LDAP environment
  name: ldap_dn
  type: string
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-repo-branches-api-nullable-team-simple-schema.json
slug: github-repo-branches-api-nullable-team-simple
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: nullable-team-simple
---
