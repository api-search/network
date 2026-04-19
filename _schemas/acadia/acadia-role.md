---
description: A job role with training requirements
layout: schema
name: Role
properties_list:
- description: Role identifier
  name: id
  type: string
- description: Role name
  name: name
  type: string
- description: Department the role belongs to
  name: department
  type: string
- description: Number of required training completions for the role
  name: requiredTrainings
  type: integer
- description: Average completion rate across employees in this role
  name: completionRate
  type: integer
provider_name: Acadia
provider_slug: acadia
schema_file: json-schema/acadia-role-schema.json
slug: acadia-role
tags:
- Connected Worker
- Knowledge Management
- Manufacturing
- Skills Management
- Training
- Workforce Development
title: Role
---
