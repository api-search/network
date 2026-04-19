---
description: ''
layout: schema
name: Workspace
properties_list:
- description: The creation date
  name: createdAt
  type: string
- description: The default ttl for the workspaces items, in seconds. If not set, the default will be set by server configuration (currently 1 year)
  name: defaultItemTtl
  type: number
- description: ''
  name: id
  type: object
- description: A list of user defined labels or tags
  name: labels
  type: array
- description: The name of the workspace, must be seen as a human readable technique id. Can not be formatted like an id. Must be unique in the platform. Auto-generated if not provided at the creation of the workspa
  name: name
  type: string
- description: Human readable workspace title for convenience
  name: title
  type: string
- description: The id of the user who own the workspace
  name: userId
  type: string
provider_name: Airbus OneAtlas
provider_slug: airbus-oneatlas
schema_file: json-schema/oneatlas-workspace-schema.json
slug: oneatlas-workspace
tags:
- Imagery
- Satellites
title: Workspace
---
