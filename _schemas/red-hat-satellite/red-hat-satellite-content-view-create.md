---
description: Parameters for creating a new content view.
layout: schema
name: ContentViewCreate
properties_list:
- description: Organization identifier.
  name: organization_id
  type: integer
- description: Name of the content view.
  name: name
  type: string
- description: Content view label (auto-generated from name if omitted).
  name: label
  type: string
- description: Description of the content view.
  name: description
  type: string
- description: Whether this is a composite content view.
  name: composite
  type: boolean
- description: Whether this is a rolling content view.
  name: rolling
  type: boolean
- description: Auto-publish composite view when a component updates.
  name: auto_publish
  type: boolean
- description: Resolve RPM dependencies during publish.
  name: solve_dependencies
  type: boolean
- description: Mark as import-only content view.
  name: import_only
  type: boolean
- description: Repository IDs to include.
  name: repository_ids
  type: array
- description: Content view version IDs for composite views.
  name: component_ids
  type: array
- description: Lifecycle environment IDs for rolling content views.
  name: environment_ids
  type: array
provider_name: Red Hat Satellite
provider_slug: red-hat-satellite
schema_file: json-schema/red-hat-satellite-content-view-create-schema.json
slug: red-hat-satellite-content-view-create
tags:
- Configuration Management
- Lifecycle Management
- Patch Management
- Subscription Management
- Systems Management
title: ContentViewCreate
---
