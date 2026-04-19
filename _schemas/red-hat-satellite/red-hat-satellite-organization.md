---
description: An organization providing multi-tenancy isolation for content, hosts, and subscriptions.
layout: schema
name: Organization
properties_list:
- description: Unique identifier for the organization.
  name: id
  type: integer
- description: Organization name.
  name: name
  type: string
- description: Unique label for the organization.
  name: label
  type: string
- description: Organization title.
  name: title
  type: string
- description: Organization description.
  name: description
  type: '[''string'', ''null'']'
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Red Hat Satellite
provider_slug: red-hat-satellite
schema_file: json-schema/red-hat-satellite-organization-schema.json
slug: red-hat-satellite-organization
tags:
- Configuration Management
- Lifecycle Management
- Patch Management
- Subscription Management
- Systems Management
title: Organization
---
