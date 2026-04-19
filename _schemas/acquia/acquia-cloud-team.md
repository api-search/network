---
description: team schema from Acquia Cloud API
layout: schema
name: Team
properties_list:
- description: The UUID of the team.
  name: uuid
  type: string
- description: The name of the team.
  name: name
  type: string
- description: The date the team was created.
  name: created_at
  type: string
- description: The date the team was last updated.
  name: updated_at
  type: string
- description: ''
  name: organization
  type: object
- description: ''
  name: _links
  type: object
provider_name: Acquia
provider_slug: acquia
schema_file: json-schema/acquia-cloud-team-schema.json
slug: acquia-cloud-team
tags:
- Content
- Experience
title: Team
---
