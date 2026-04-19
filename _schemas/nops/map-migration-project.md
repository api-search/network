---
description: A MAP Migration project represents an AWS Migration Acceleration Program engagement signed by the customer with AWS, tracking the overall migration effort.
layout: schema
name: nOps MAP Migration Project
properties_list:
- description: The unique identifier of the MAP Migration project.
  name: id
  type: integer
- description: The name of the MAP Migration project.
  name: name
  type: string
- description: The current status of the project.
  name: status
  type: string
- description: Timestamp when the project was created.
  name: created_at
  type: string
- description: Timestamp when the project was last updated.
  name: updated_at
  type: string
provider_name: nOps
provider_slug: nops
schema_file: json-schema/map-migration-project.json
slug: map-migration-project
tags:
- Costs
- FinOps
title: nOps MAP Migration Project
---
