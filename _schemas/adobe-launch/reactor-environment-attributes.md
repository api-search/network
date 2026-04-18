---
description: ''
layout: schema
name: EnvironmentAttributes
properties_list:
- description: The name of the environment.
  name: name
  type: string
- description: The environment stage.
  name: stage
  type: string
- description: Whether the build is delivered as a ZIP archive.
  name: archive
  type: boolean
- description: The URL path appended to the host domain for deployment.
  name: path
  type: string
- description: The custom library filename.
  name: library_name
  type: string
- description: The custom library path.
  name: library_path
  type: string
- description: A unique token for the environment.
  name: token
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Adobe Launch
provider_slug: adobe-launch
schema_file: json-schema/reactor-environment-attributes-schema.json
slug: reactor-environment-attributes
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
title: EnvironmentAttributes
---
