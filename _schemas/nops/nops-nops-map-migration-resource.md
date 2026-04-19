---
description: ''
layout: schema
name: MapMigrationResource
properties_list:
- description: The unique identifier of the resource.
  name: id
  type: integer
- description: The type of the AWS resource.
  name: resource_type
  type: string
- description: The AWS resource identifier.
  name: resource_id
  type: string
- description: The ID of the parent MAP Migration project.
  name: project_id
  type: integer
provider_name: nOps
provider_slug: nops
schema_file: json-schema/nops-nops-map-migration-resource-schema.json
slug: nops-nops-map-migration-resource
tags:
- Costs
- FinOps
title: MapMigrationResource
---
