---
description: A content view defining a curated set of repositories and content available to hosts.
layout: schema
name: ContentView
properties_list:
- description: Unique identifier for the content view.
  name: id
  type: integer
- description: Name of the content view.
  name: name
  type: string
- description: Unique label for the content view (auto-generated from name).
  name: label
  type: string
- description: Description of the content view.
  name: description
  type: '[''string'', ''null'']'
- description: Organization this content view belongs to.
  name: organization_id
  type: integer
- description: ''
  name: organization
  type: object
- description: Whether this is a composite content view combining other content view versions.
  name: composite
  type: boolean
- description: Whether this is a rolling content view.
  name: rolling
  type: boolean
- description: Whether composite content views auto-publish when a component is updated.
  name: auto_publish
  type: boolean
- description: Whether RPM dependencies are resolved during publish.
  name: solve_dependencies
  type: boolean
- description: Whether this content view is only for upstream imports.
  name: import_only
  type: boolean
- description: If generated, indicates the purpose (e.g., import or export).
  name: generated_for
  type: '[''string'', ''null'']'
- description: Whether this is the default content view (every organization has one).
  name: default
  type: boolean
- description: Identifiers of repositories in this content view.
  name: repository_ids
  type: array
- description: Repositories included in this content view.
  name: repositories
  type: array
- description: Content view version IDs for composite content views.
  name: component_ids
  type: array
- description: Published versions of this content view.
  name: versions
  type: array
- description: Lifecycle environments this content view is in.
  name: environments
  type: array
- description: Activation keys using this content view.
  name: activation_keys
  type: array
- description: Next version number to be published.
  name: next_version
  type: string
- description: Timestamp of the last publish.
  name: last_published
  type: '[''string'', ''null'']'
- description: Latest published version number.
  name: latest_version
  type: '[''string'', ''null'']'
- description: Identifier of the latest published version.
  name: latest_version_id
  type: '[''integer'', ''null'']'
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Red Hat Satellite
provider_slug: red-hat-satellite
schema_file: json-schema/red-hat-satellite-content-view-schema.json
slug: red-hat-satellite-content-view
tags:
- Configuration Management
- Lifecycle Management
- Patch Management
- Subscription Management
- Systems Management
title: ContentView
---
