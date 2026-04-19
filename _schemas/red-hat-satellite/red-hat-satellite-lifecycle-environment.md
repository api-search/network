---
description: A lifecycle environment defining a stage in the content promotion path.
layout: schema
name: LifecycleEnvironment
properties_list:
- description: Unique identifier for the lifecycle environment.
  name: id
  type: integer
- description: Name of the lifecycle environment.
  name: name
  type: string
- description: Unique label for the lifecycle environment.
  name: label
  type: string
- description: Description of the lifecycle environment.
  name: description
  type: '[''string'', ''null'']'
- description: Organization this environment belongs to.
  name: organization_id
  type: integer
- description: ''
  name: organization
  type: object
- description: Whether this is the Library environment.
  name: library
  type: boolean
- description: Prior environment in the promotion path.
  name: prior
  type: object
- description: Successor environment in the promotion path.
  name: successor
  type: '[''object'', ''null'']'
- description: Content counts for this environment.
  name: counts
  type: object
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Red Hat Satellite
provider_slug: red-hat-satellite
schema_file: json-schema/red-hat-satellite-lifecycle-environment-schema.json
slug: red-hat-satellite-lifecycle-environment
tags:
- Configuration Management
- Lifecycle Management
- Patch Management
- Subscription Management
- Systems Management
title: LifecycleEnvironment
---
