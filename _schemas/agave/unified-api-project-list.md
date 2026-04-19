---
description: Paginated list of projects.
layout: schema
name: ProjectList
properties_list:
- description: Array of project records.
  name: data
  type: array
- description: Cursor for the next page of results.
  name: next_cursor
  type: string
- description: Number of records returned.
  name: count
  type: integer
provider_name: Agave
provider_slug: agave
schema_file: json-schema/unified-api-project-list-schema.json
slug: unified-api-project-list
tags:
- Accounting
- Construction
- Integration
title: ProjectList
---
