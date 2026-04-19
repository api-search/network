---
description: A set of LookML models that can be assigned to a role
layout: schema
name: ModelSet
properties_list:
- description: Unique numeric identifier
  name: id
  type: integer
- description: Display name
  name: name
  type: string
- description: List of model names included in this set
  name: models
  type: array
- description: Whether this is a built-in model set
  name: built_in
  type: boolean
- description: Whether this grants access to all models
  name: all_access
  type: boolean
- description: Relative URL
  name: url
  type: string
provider_name: Looker
provider_slug: looker
schema_file: json-schema/looker-model-set-schema.json
slug: looker-model-set
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
title: ModelSet
---
