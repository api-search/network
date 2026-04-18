---
description: Custom repository roles created by organization owners
layout: schema
name: organization-custom-repository-role
properties_list:
- description: The unique identifier of the custom role.
  name: id
  type: integer
- description: The name of the custom role.
  name: name
  type: string
- description: A short description about who this role is for or what permissions it grants.
  name: description
  type: string
- description: The system role from which this role inherits permissions.
  name: base_role
  type: string
- description: A list of additional permissions included in this role.
  name: permissions
  type: array
- description: ''
  name: organization
  type: object
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: GitHub
provider_slug: github
schema_file: json-schema/github-organizations-organization-custom-repository-role-schema.json
slug: github-organizations-organization-custom-repository-role
tags:
- Code
- Pipelines
- Platform
- Software Development
- Source Control
- T1
title: organization-custom-repository-role
---
