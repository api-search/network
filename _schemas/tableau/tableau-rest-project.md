---
description: ''
layout: schema
name: Project
properties_list:
- description: The unique identifier for the project.
  name: id
  type: string
- description: The name of the project.
  name: name
  type: string
- description: A description of the project.
  name: description
  type: string
- description: The ID of the parent project. If null, this is a top-level project.
  name: parentProjectId
  type: '[''string'', ''null'']'
- description: The permissions model for the project.
  name: contentPermissions
  type: string
- description: The date and time the project was created.
  name: createdAt
  type: string
- description: The date and time the project was last updated.
  name: updatedAt
  type: string
- description: ''
  name: owner
  type: object
- description: Whether this is a top-level project.
  name: topLevelProject
  type: boolean
provider_name: Tableau
provider_slug: tableau
schema_file: json-schema/tableau-rest-project-schema.json
slug: tableau-rest-project
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
title: Project
---
