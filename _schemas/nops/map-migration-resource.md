---
description: A MAP Migration resource represents an individual AWS resource that is part of a MAP Migration project, tracked for migration and cost attribution.
layout: schema
name: nOps MAP Migration Resource
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
schema_file: json-schema/map-migration-resource.json
slug: map-migration-resource
tags:
- Costs
- FinOps
title: nOps MAP Migration Resource
---
